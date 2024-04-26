from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QFontDatabase

import sys
import threading
from openpyxl import Workbook
from openpyxl.utils.cell import get_column_interval
from openpyxl.styles import (
    Alignment, Font
)

from common_func import send_message_box, SMBOX_ICON_TYPE, get_about_text, get_rules_text, get_current_unix_time
from ui.interface import Ui_MainWindow
from enums import JOB_TYPE
from config_parser.CConfig import CConfig, MAX_PALLET_PLACES

from components.CPalletInfoBox import CPalletInfoBOX
from components.CPalletLabel import CPalletLabel
from components.CControlPanel import CControlPanel
from components.CSNInput import CSNinput
from components.CPallet import CPallet

from sql.CSQLQuerys import CSQLQuerys
from sql.enums import CONNECT_DB_TYPE
from sql.sql_data import SQL_PALLET_SCANNED, SQL_TABLE_TV_CONFIG, SQL_TABLE_ASSEMBLED_TV


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"  # Менять при каждом обновлении любой из подпрограмм

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Сканирование паллетов TCL ООО Квант 2024 v{self.__base_program_version} '
                            f'[Режим: создание паллет]')

        # self.ui.centralwidget.setEnabled(False)  # на всякий блокирнём интерфейс
        # config ------------------------------

        self.cconfig = CConfig()
        if self.cconfig.load_data() is False:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text="Ошибка в файле конфигурации!\n"
                                  "Один или несколько параметров ошибочны!\n\n"
                                  "Обратитесь к системному администратору.",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=lambda: self.set_close())
            return
        # ---------------------------------------
        program_job_type = self.cconfig.get_soft_job_type()
        self.program_job_type = program_job_type

        self.auto_complect = self.cconfig.get_pallet_auto_completed()
        # classes

        max_places_in_pallets = self.cconfig.get_pallet_max_places()
        self.cpallets_box = CPalletInfoBOX(self.ui)
        self.cpallets_box.set_max_place(max_places_in_pallets)
        self.cpallets_box.set_block_frame()
        self.cpallets_box.clear_box()

        self.cpallet_label = CPalletLabel(self.ui)
        pallet_template = self.cconfig.get_pallet_template()
        self.cpallet_label.set_default_text(pallet_template)
        self.cpallet_label.clear()

        self.ccontrol_box = CControlPanel(self.ui)
        self.ccontrol_box.set_max_places(0)
        self.ccontrol_box.set_last_places(0)

        self.csn_input = CSNinput(self.ui)
        tv_template = self.cconfig.get_tv_template()
        self.csn_input.set_clear_label()

        # todo Запрет на совпадение шаблонов
        if pallet_template == tv_template:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text="Ошибка в заданных шаблонах!\n"
                                  "Шаблоны ТВ и паллета совпадают!\n\n"
                                  "Обратитесь к системному администратору, так быть не должно.",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=lambda: self.set_close())
            return

        self.cpallet = CPallet()
        self.cpallet.set_pallet_template(pallet_template)
        self.cpallet.set_tv_template(tv_template)

        # slots

        if self.program_job_type == JOB_TYPE.MAIN:
            self.ui.pushButton_set_cancel.clicked.connect(lambda: self.on_user_pressed_pallet_cancel())
            self.ui.pushButton_set_complete.clicked.connect(lambda: self.on_user_pressed_pallet_complete())

        self.csn_input.disabled_btns()

        # Если инфо мод то глушим ненужное
        if program_job_type == JOB_TYPE.INFO:
            self.setWindowTitle(f'Сканирование паллетов TCL ООО Квант 2024 v{self.__base_program_version} '
                                f'[Режим: демонстрация укомплектованности паллет]')

            self.ccontrol_box.disable_place_info()
            self.ccontrol_box.set_last_places(0)
            self.ccontrol_box.set_max_places(0)
            #

        self.ui.pushButton_info.clicked.connect(lambda: self.on_user_pressed_info_btn())

        self.ui.le_main.returnPressed.connect(lambda: self.on_user_input_sn_or_pallet())

        del self.cconfig

    def on_user_input_sn_or_pallet(self):
        input_text = self.csn_input.get_current_text()
        input_text = input_text.upper().replace(" ", "")

        if len(input_text) < 4:
            self.csn_input.set_clear_label()
            return
        template_pallet = self.cpallet.get_pallet_template()
        template_tv = self.cpallet.get_tv_template()

        if AntiFlood.is_flood() is True:
            return

        if self.program_job_type == JOB_TYPE.INFO:  # сканировка демонстрация

            self.load_info_mode(input_text, template_pallet)

        else:  # сканировка паллета для создания
            self.load_job_mode(input_text, template_tv, template_pallet)

    def load_job_mode(self, input_text, template_tv, template_pallet):

        if self.program_job_type == JOB_TYPE.MAIN:  # Привязка
            if self.cpallet.is_pallet_chosen():  # Палет выбран
                chosen_pallet = self.cpallet.get_pallet_chosen()
                if self.cpallet.is_pattern_match(template_tv, input_text):
                    csql = CSQLQuerys()
                    try:
                        result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                        if result_connect is True:
                            if csql.is_created_pallet(chosen_pallet) is False:
                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                 text=f"Указанный паллет '{chosen_pallet}' не найден!\n"
                                                      f"Данные паллета сброшены!\n\n"
                                                      f"Внимание! Перескинируйте все телевизоры на другой паллет!!!",
                                                 title="Внимание!",
                                                 variant_yes="Закрыть", variant_no="", callback=None)

                                self.clear_current_pallet()
                                return
                    except:
                        self.send_error_message(
                            "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                            "Обратитесь к системному администратору!\n\n"
                            "Код ошибки: 'on_user_input_sn_or_pallet -> is_created_pallet'")
                        return
                    finally:
                        csql.disconnect_from_db()

                    #  Паттерн совпал с заданным
                    empty_places = self.cpallets_box.get_pallet_empty_places()
                    # max_places = self.cpallets_box.get_max_places()

                    if empty_places <= 0:
                        if self.auto_complect is True:
                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                             text=f"Указанный паллет '{chosen_pallet}' уже сформирован полностью!\n"
                                                  f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                  f"Паллет готов к отгрузке!",
                                             title="Успех!",
                                             variant_yes="Закрыть", variant_no="", callback=None)

                            self.clear_current_pallet()
                            # todo Паллет обнулён из за переполнения
                        else:  # автокомплект отключен
                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                             text=f"Указанный паллет '{chosen_pallet}' уже сформирован полностью!\n"
                                                  f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                  f"Нажмите кнопку 'Завершить паллет', что бы закрыть выбранный паллет!",
                                             title="Успех!",
                                             variant_yes="Закрыть", variant_no="", callback=None)
                            # todo Паллет набился но не обнулён, так как авто комплект отключен
                        return True

                    # Готово todo Проверка на наличие копии в паллете
                    # Готово todo проверка на наличие этого телика в другом паллете с теликами
                    # Готово TODO проверка наличия созданого в assembled телека и его прохождение через станцию проверка комплектности (по дате)
                    # Готово TODO Вставка отсканированного тв в бд
                    # Готово Проверить само существование паллета в бд -> Сделано вверху

                    if self.cpallets_box.get_place_index_from_tv_sn(
                            input_text) == -1:  # Проверка только в текущем паллете программы

                        tv_fk = None

                        csql = CSQLQuerys()
                        try:
                            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                            if result_connect is True:
                                result = csql.get_pallet_id_from_tv_sn(input_text)
                                if result is not False:
                                    old_pallete_code = result

                                    if old_pallete_code is not None:
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                         text=f"Указанный серийный номер '{input_text}' найден в другом паллете '{old_pallete_code}' !\n"
                                                              f"Позовите технолога!",
                                                         title="Внимание!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)

                                        self.csn_input.set_clear_label()
                                        return

                                result = csql.get_tv_info(input_text)
                                if result is not False:
                                    # нет смысла в том что ниже, так как телек просто не создатся без сканировки серийника на линии
                                    # scan_time = result.get(SQL_TABLE_ASSEMBLED_TV.fd_sn_scan_time, None)
                                    # if scan_time is None:
                                    #     send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                    #                      text=f"Указанный серийный номер '{input_text}' не прошёл "
                                    #                           f"первичную сканировку !\n"
                                    #                           f"Позовите технолога!\n\n",
                                    #                      title="Внимание!",
                                    #                      variant_yes="Закрыть", variant_no="", callback=None)
                                    #
                                    #     self.csn_input.set_clear_label()
                                    #     return
                                    # sn_scan_time = result.get(SQL_TABLE_ASSEMBLED_TV.fd_sn_scan_time, None)
                                    # if sn_scan_time is None:
                                    #     send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                    #                      text=f"Указанный серийный номер '{input_text}' не прошёл "
                                    #                           f"привязку серийного номера !\n"
                                    #                           f"Позовите технолога!\n\n",
                                    #                      title="Внимание!",
                                    #                      variant_yes="Закрыть", variant_no="", callback=None)
                                    #
                                    #     self.csn_input.set_clear_label()
                                    #     return

                                    complect_check_time = result.get(SQL_TABLE_ASSEMBLED_TV.fd_completed_scan_time,
                                                                     None)
                                    if complect_check_time is None:
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                         text=f"Указанный серийный номер '{input_text}' не прошёл "
                                                              f"проверку комплектности на упаковке !\n"
                                                              f"Позовите технолога!",
                                                         title="Внимание!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)

                                        self.csn_input.set_clear_label()
                                        return
                                    tv_fk = result.get(SQL_TABLE_TV_CONFIG.fd_tv_id, None)
                                else:
                                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                     text=f"Указанный серийный номер '{input_text}' не найден в числе "
                                                          f"собранных телевизоров!\n"
                                                          f"Позовите технолога!",
                                                     title="Внимание!",
                                                     variant_yes="Закрыть", variant_no="", callback=None)

                                    self.csn_input.set_clear_label()
                                    return

                        except Exception as err:
                            self.send_error_message(
                                "Во время получения данных устройства возникла ошибка.\n"
                                "Обратитесь к системному администратору!\n\n"
                                "Код ошибки: 'load_job_mode -> get_pallet_id_from_tv_sn'")
                            return
                        finally:
                            csql.disconnect_from_db()
                        if tv_fk is not None and self.cpallets_box.set_sn_in_pallet(input_text) is True:
                            pallet_index = None
                            csql = CSQLQuerys()
                            try:
                                result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                                if result_connect is True:
                                    result = csql.insert_scanned_tv_on_pallet(chosen_pallet, input_text, tv_fk)
                                    if result is not False:
                                        pallet_index = result
                            except:
                                self.send_error_message(
                                    "Во время создания паллета в БД возникла ошибка.\n"
                                    "Обратитесь к системному администратору!\n\n"
                                    "Код ошибки: 'load_job_mode -> insert_scanned_tv_on_pallet'")
                                return
                            finally:
                                csql.disconnect_from_db()

                            if isinstance(pallet_index, int):
                                empty_places -= 1
                                self.ccontrol_box.set_last_places(empty_places)
                                self.csn_input.set_clear_label()

                                # todo SN заведён

                                if empty_places <= 0:

                                    if self.auto_complect is True:
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                                         text=f"Указанный паллет '{chosen_pallet}' сформирован!\n"
                                                              f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                              f"Паллет готов к отгрузке!",
                                                         title="Успех!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)

                                        self.clear_current_pallet()
                                        # todo Паллет обнулён из за переполнения
                                    else:  # автокомплект отключен
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                                         text=f"Указанный паллет '{chosen_pallet}' сформирован!\n"
                                                              f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                              f"Нажмите кнопку 'Завершить паллет', что бы закрыть выбранный паллет!",
                                                         title="Успех!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)
                                        # todo Паллет набился но не обнулён, так как авто комплект отключен
                                return True

                            else:
                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                 text=f"В обработчике привязки SN к паллету произошла ошибка. Паллет отвязан от SN !\n"
                                                      f"Позовите технолога!!!",
                                                 title="Внимание!",
                                                 variant_yes="Закрыть", variant_no="", callback=None)
                                self.csn_input.set_clear_label()

                                # На всякий отвязка
                                # Отвязка SQL
                                csql = CSQLQuerys()
                                try:
                                    result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                                    if result_connect is True:
                                        csql.delete_tv_sn_from_pallet_scanned(chosen_pallet, input_text)

                                except Exception as err:
                                    print(f"Ошибка: {err}")
                                    return
                                finally:
                                    csql.disconnect_from_db()

                                # Отвязка в паллете
                                sn_index = self.cpallets_box.get_place_index_from_tv_sn(input_text)
                                if sn_index != -1:
                                    self.cpallets_box.clear_field(sn_index)
                                return False
                    else:
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"В паллете '{chosen_pallet}' уже есть телевизор с указанным серийным номером '{input_text}' !",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        self.csn_input.set_clear_label()
                        return

                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Шаблон серийного номера телевизора не совпал с указанным серийным номером! '{template_tv}' -> | '{input_text}'",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.csn_input.set_clear_label()
                    return
            else:  # Если паллет не выбран то

                if self.cpallet.is_pattern_match(template_pallet, input_text):

                    success_load = False
                    csql = CSQLQuerys()
                    try:
                        # Проверяем паллет на наличие
                        # Если палет есть то просто грузим всё что в нём
                        # Если паллета нет то создаём и переходим в набивание
                        result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                        if result_connect is True:
                            if csql.is_created_pallet(input_text) is True:
                                if self.load_sns_in_pallet(input_text) is True:
                                    success_load = True
                            else:  # если паллета нет - создаём
                                if csql.create_new_pallet(input_text) is True:
                                    if csql.is_pallet_have_any_sn(input_text) is False:
                                        success_load = True
                                    else:
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                         text=f"В новом паллете '{input_text}' обнаружены телевизоры "
                                                              f"!!!\n\n"
                                                              f"Так быть не должно! Позовите технолога!!!",
                                                         title="Внимание!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)
                                        self.csn_input.set_clear_label()

                                        # сбрасываем бокс
                                        self.clear_current_pallet()
                                        return False

                    except Exception as err:
                        self.send_error_message(
                            "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                            "Обратитесь к системному администратору!\n\n"
                            "Код ошибки: 'on_user_input_sn_or_pallet -> get_info_data'")
                        print(f"Ошибка: {err}")
                        return
                    finally:
                        csql.disconnect_from_db()

                    if success_load is True:
                        empty_places = self.cpallets_box.get_pallet_empty_places()

                        max_places = self.cpallets_box.get_max_places()
                        self.ccontrol_box.set_max_places(max_places)
                        self.ccontrol_box.set_last_places(empty_places)
                        self.cpallet_label.set_name(input_text)
                        if empty_places > 0:  # Места ещё есть

                            self.cpallet.set_pallet_chosen(input_text)
                            self.csn_input.set_clear_label()
                            self.csn_input.enable_btns()
                            # todo Паллет заведён
                            return True
                        else:  # Мест нет

                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                             text=f"В паллете '{input_text}' больше нет места. Выбор паллета сброшен!!!",
                                             title="Внимание!",
                                             variant_yes="Закрыть", variant_no="", callback=None)
                            self.csn_input.set_clear_label()

                            # сбрасываем бокс
                            self.clear_current_pallet()
                            return False

                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.csn_input.set_clear_label()
        return False

    def load_info_mode(self, input_text, template_pallet):
        if self.cpallet.is_pattern_match(template_pallet, input_text):

            if self.cpallet.get_pallet_chosen() != input_text:

                if self.load_sns_in_pallet(input_text) is True:
                    self.cpallet.set_pallet_chosen(input_text)
                    self.cpallet_label.set_name(input_text)
                    self.csn_input.set_clear_label()
                    return True

            else:
                pass
                # ничего нет так как палет указан тот же
        else:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            self.csn_input.set_clear_label()

        return False

    def load_sns_in_pallet(self, pallette_code: str) -> bool:

        csql = CSQLQuerys()
        try:
            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
            if result_connect is True:

                if csql.is_created_pallet(pallette_code) is True:

                    result = csql.get_pallet_info(pallette_code)
                    if result is not False and len(result) > 0:
                        count_not_find = 0
                        count = 0
                        self.cpallets_box.clear_box()
                        for item in result:
                            tv_sn = item.get(SQL_PALLET_SCANNED.fd_tv_sn, None)
                            if tv_sn is not None:
                                self.cpallets_box.set_sn_in_pallet(tv_sn)
                                count += 1
                            else:
                                count_not_find += 1

                        if count_not_find > 0:
                            self.send_error_message(
                                "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                                "Один из SN на паллете = 'None'!\n\n"
                                "Код ошибки: 'on_user_input_sn_or_pallet -> get_info_data'")
                            return False

                        if count > 0:
                            # todo Паллет открыт - инфа
                            return True

                    else:
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Указанный паллет '{pallette_code}' найден, но не имеет привязанных телевизоров!",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                else:

                    if self.program_job_type == JOB_TYPE.INFO:
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Указанный паллет '{pallette_code}' не найден!",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        return False
                    else:
                        return True
        except Exception:
            self.send_error_message(
                "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                "Обратитесь к системному администратору!\n\n"
                "Код ошибки: 'load_sns_in_pallet -> get_sn_data'")
        finally:
            csql.disconnect_from_db()

        return False

    def on_user_pressed_pallet_complete(self):

        if AntiFlood.is_flood() is True:
            return

        if not self.cpallet.is_pallet_chosen():
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"Вы не ввели номер паллета.",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            return

        if self.program_job_type == JOB_TYPE.INFO:
            return

        pallette_code = self.cpallet.get_pallet_chosen()

        empty_places = self.cpallets_box.get_pallet_empty_places()
        max_places = self.cpallets_box.get_max_places()

        if max_places == 0:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"С паллетом '{pallette_code}' возникла ошибка.",
                             title="Внимание! Позовите технолога!!!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            return
        if empty_places == max_places:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"На паллете '{pallette_code}' нет телевизоров.",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            return

        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                         text=(f"Вы уверены, что хотите закончить формирование паллета '{pallette_code}' ?\n\n"
                               f"Продолжить формирование можно в любой момент, просто введите номер этого паллета."),
                         title="Внимание!",
                         variant_yes="Да", variant_no="Нет",
                         callback=self.on_user_clicked_variant_btn_pallette_complete)

        return True

    def on_user_clicked_variant_btn_pallette_complete(self, val):
        if val.text() == "Да":
            self.csn_input.set_clear_label()
            self.clear_current_pallet()
        else:
            pass

    def on_user_pressed_pallet_cancel(self):

        if AntiFlood.is_flood() is True:
            return
        if not self.cpallet.is_pallet_chosen():
            return

        if self.program_job_type == JOB_TYPE.INFO:
            return

    @classmethod
    def on_user_pressed_info_btn(cls):
        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                         text=f"{get_about_text()}"
                              f"\n"
                              f"\n"
                              f"{get_rules_text()}",
                         title="О программе",
                         variant_yes="Закрыть", variant_no="")

    def send_error_message(self, text: str):
        self.set_block_interface()
        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                         text=text,
                         title="Фатальная ошибка",
                         variant_yes="Закрыть программу", variant_no="", callback=self.set_close())

    def clear_current_pallet(self):
        self.ccontrol_box.set_max_places(0)
        self.ccontrol_box.set_last_places(0)
        self.cpallet_label.clear()
        self.csn_input.disabled_btns()
        self.cpallet.set_pallet_chosen("")
        self.csn_input.set_clear_label()
        self.cpallets_box.clear_box()

    def set_block_interface(self):
        self.ui.centralwidget.setDisabled(True)

    @staticmethod
    def set_close():
        sys.exit()


class AntiFlood:
    """Антифлуд от флудерского софта и флудерастов"""
    __anti_flood_load_data = 0
    __connects = 0
    __max_connects = 5

    @classmethod
    def is_flood(cls):
        unix = get_current_unix_time()
        if cls.__anti_flood_load_data != unix:
            cls.__connects = 0
            cls.__anti_flood_load_data = unix
        cls.__connects += 1

        if cls.__connects > cls.__max_connects:
            return True

        return False
