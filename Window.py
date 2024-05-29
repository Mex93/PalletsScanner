from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

import sys

from common_func import (send_message_box, SMBOX_ICON_TYPE,
                         get_about_text, get_rules_text,
                         get_current_unix_time, is_pallet_text_valid,
                         is_tv_sn_valid)
from ui.interface import Ui_MainWindow
from enums import JOB_TYPE, REPEAT_TV_ERROR_TYPES
from config_parser.CConfig import CConfig

from components.CPalletInfoBox import CPalletInfoBOX
from components.CPalletLabel import CPalletLabel
from components.CControlPanel import CControlPanel
from components.CSNInput import CSNinput
from components.CPallet import CPallet
from components.CExcelLog import CExcelLog
from sql.CSQLQuerys import CSQLQuerys
from sql.enums import CONNECT_DB_TYPE
from sql.sql_data import SQL_PALLET_SCANNED, SQL_TABLE_TV_CONFIG, SQL_TABLE_ASSEMBLED_TV
import datetime

NON_DELETE_HOURS = 4


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.4"  # Менять при каждом обновлении
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_block_interface()
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Формирование паллетов готовой продукции ООО Квант 2024 v{self.__base_program_version} '
                            f'[Режим: Создание паллет]')

        # self.ui.centralwidget.setEnabled(False)  # на всякий блокирнём интерфейс
        # config ------------------------------

        self.cconfig = CConfig()
        if self.cconfig.load_data() is False:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text="Ошибка в файле конфигурации!\n"
                                  "Один или несколько параметров ошибочны!\n\n"
                                  "Позовите технолога!",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=lambda: self.set_close())
            return

        # ---------------------------------------
        try:
            self.assembled_line = self.cconfig.get_current_line()
            if self.assembled_line is None:
                raise ValueError("Неверно выставлен номер производственной линии!!")

            self.repeat_tv_error_type = self.cconfig.get_repeat_tv_error_type()
            program_job_type = self.cconfig.get_soft_job_type()
            self.auto_complect = self.cconfig.get_pallet_auto_completed()
            max_places_in_pallets = self.cconfig.get_pallet_max_places()
            pallet_template = self.cconfig.get_pallet_template()
            tv_template = self.cconfig.get_tv_template()

            self.program_job_type = program_job_type
        except Exception as err:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text="Ошибка в файле конфигурации!\n"
                                  "Один или несколько параметров ошибочны!\n\n"
                                  "Позовите технолога!\n\n"
                                  f"Ошибка: '{err}'",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=lambda: self.set_close())
            return
        # classes

        self.cpallets_box = CPalletInfoBOX(self.ui)
        self.cpallets_box.set_max_place(max_places_in_pallets)
        self.cpallets_box.set_block_frame()
        self.cpallets_box.clear_box()

        self.cpallet_label = CPalletLabel(self.ui)
        self.cpallet_label.set_default_text(pallet_template)
        self.cpallet_label.clear()

        self.ccontrol_box = CControlPanel(self.ui)
        self.ccontrol_box.set_max_places(0)
        self.ccontrol_box.set_last_places(0)

        self.csn_input = CSNinput(self.ui)

        self.csn_input.set_clear_label()

        # todo Запрет на совпадение шаблонов
        if pallet_template == tv_template:
            self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
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
            self.ui.pushButton_set_cancel.clicked.connect(lambda: self.on_user_pressed_pallet_complete("cancel"))
            self.ui.pushButton_set_complete.clicked.connect(lambda: self.on_user_pressed_pallet_complete("success"))

        self.csn_input.disabled_btns()

        # Если инфо мод то глушим ненужное
        if program_job_type == JOB_TYPE.INFO:
            self.setWindowTitle(
                f'Формирование паллетов готовой продукции ООО Квант 2024 v{self.__base_program_version} '
                f'[Режим: Демонстрация укомплектованности паллет]')

            self.ccontrol_box.disable_place_info()
            # self.ccontrol_box.set_last_places(0)
            # self.ccontrol_box.set_max_places(0)
            self.ccontrol_box.set_count_in_pallet(0)
            self.ccontrol_box.set_clear_last_place()
            #

        self.ui.pushButton_info.clicked.connect(lambda: self.on_user_pressed_info_btn())

        self.ui.pushButton_field_0.clicked.connect(lambda: self.on_clicked_on_pallet(0))
        self.ui.pushButton_field_1.clicked.connect(lambda: self.on_clicked_on_pallet(1))
        self.ui.pushButton_field_2.clicked.connect(lambda: self.on_clicked_on_pallet(2))
        self.ui.pushButton_field_3.clicked.connect(lambda: self.on_clicked_on_pallet(3))
        self.ui.pushButton_field_4.clicked.connect(lambda: self.on_clicked_on_pallet(4))
        self.ui.pushButton_field_5.clicked.connect(lambda: self.on_clicked_on_pallet(5))
        self.ui.pushButton_field_6.clicked.connect(lambda: self.on_clicked_on_pallet(6))
        self.ui.pushButton_field_7.clicked.connect(lambda: self.on_clicked_on_pallet(7))
        self.ui.pushButton_field_8.clicked.connect(lambda: self.on_clicked_on_pallet(8))
        self.ui.pushButton_field_9.clicked.connect(lambda: self.on_clicked_on_pallet(9))
        self.ui.pushButton_field_10.clicked.connect(lambda: self.on_clicked_on_pallet(10))
        self.ui.pushButton_field_11.clicked.connect(lambda: self.on_clicked_on_pallet(11))
        self.ui.pushButton_field_12.clicked.connect(lambda: self.on_clicked_on_pallet(12))
        self.ui.pushButton_field_13.clicked.connect(lambda: self.on_clicked_on_pallet(13))
        self.ui.pushButton_field_14.clicked.connect(lambda: self.on_clicked_on_pallet(14))
        self.ui.pushButton_field_15.clicked.connect(lambda: self.on_clicked_on_pallet(15))
        self.ui.pushButton_field_16.clicked.connect(lambda: self.on_clicked_on_pallet(16))
        self.ui.pushButton_field_17.clicked.connect(lambda: self.on_clicked_on_pallet(17))
        self.ui.pushButton_field_18.clicked.connect(lambda: self.on_clicked_on_pallet(18))
        self.ui.pushButton_field_19.clicked.connect(lambda: self.on_clicked_on_pallet(19))
        self.ui.pushButton_field_20.clicked.connect(lambda: self.on_clicked_on_pallet(20))
        self.ui.pushButton_field_21.clicked.connect(lambda: self.on_clicked_on_pallet(21))
        self.ui.pushButton_field_22.clicked.connect(lambda: self.on_clicked_on_pallet(22))
        self.ui.pushButton_field_23.clicked.connect(lambda: self.on_clicked_on_pallet(23))
        self.ui.pushButton_field_24.clicked.connect(lambda: self.on_clicked_on_pallet(24))
        self.ui.pushButton_field_25.clicked.connect(lambda: self.on_clicked_on_pallet(25))
        self.ui.pushButton_field_26.clicked.connect(lambda: self.on_clicked_on_pallet(26))
        self.ui.pushButton_field_27.clicked.connect(lambda: self.on_clicked_on_pallet(27))
        self.ui.pushButton_field_28.clicked.connect(lambda: self.on_clicked_on_pallet(28))
        self.ui.pushButton_field_29.clicked.connect(lambda: self.on_clicked_on_pallet(29))
        self.ui.pushButton_field_30.clicked.connect(lambda: self.on_clicked_on_pallet(30))
        self.ui.pushButton_field_31.clicked.connect(lambda: self.on_clicked_on_pallet(31))
        self.ui.pushButton_field_32.clicked.connect(lambda: self.on_clicked_on_pallet(32))
        self.ui.pushButton_field_33.clicked.connect(lambda: self.on_clicked_on_pallet(33))
        self.ui.pushButton_field_34.clicked.connect(lambda: self.on_clicked_on_pallet(34))
        self.ui.pushButton_field_35.clicked.connect(lambda: self.on_clicked_on_pallet(35))
        self.ui.pushButton_field_36.clicked.connect(lambda: self.on_clicked_on_pallet(36))
        self.ui.pushButton_field_37.clicked.connect(lambda: self.on_clicked_on_pallet(37))
        self.ui.pushButton_field_38.clicked.connect(lambda: self.on_clicked_on_pallet(38))
        self.ui.pushButton_field_39.clicked.connect(lambda: self.on_clicked_on_pallet(39))
        self.ui.pushButton_field_40.clicked.connect(lambda: self.on_clicked_on_pallet(40))
        self.ui.pushButton_field_41.clicked.connect(lambda: self.on_clicked_on_pallet(41))
        self.ui.pushButton_field_42.clicked.connect(lambda: self.on_clicked_on_pallet(42))
        self.ui.pushButton_field_43.clicked.connect(lambda: self.on_clicked_on_pallet(43))
        self.ui.pushButton_field_44.clicked.connect(lambda: self.on_clicked_on_pallet(44))
        self.ui.pushButton_field_45.clicked.connect(lambda: self.on_clicked_on_pallet(45))
        self.ui.pushButton_field_46.clicked.connect(lambda: self.on_clicked_on_pallet(46))
        self.ui.pushButton_field_47.clicked.connect(lambda: self.on_clicked_on_pallet(47))
        self.ui.pushButton_field_48.clicked.connect(lambda: self.on_clicked_on_pallet(48))
        self.ui.pushButton_field_49.clicked.connect(lambda: self.on_clicked_on_pallet(49))
        self.ui.pushButton_field_50.clicked.connect(lambda: self.on_clicked_on_pallet(50))
        self.ui.pushButton_field_51.clicked.connect(lambda: self.on_clicked_on_pallet(51))
        self.ui.pushButton_field_52.clicked.connect(lambda: self.on_clicked_on_pallet(52))
        self.ui.pushButton_field_53.clicked.connect(lambda: self.on_clicked_on_pallet(53))
        self.ui.pushButton_field_54.clicked.connect(lambda: self.on_clicked_on_pallet(54))
        self.ui.pushButton_field_55.clicked.connect(lambda: self.on_clicked_on_pallet(55))
        self.ui.pushButton_field_56.clicked.connect(lambda: self.on_clicked_on_pallet(56))
        self.ui.pushButton_field_57.clicked.connect(lambda: self.on_clicked_on_pallet(57))
        self.ui.pushButton_field_58.clicked.connect(lambda: self.on_clicked_on_pallet(58))
        self.ui.pushButton_field_59.clicked.connect(lambda: self.on_clicked_on_pallet(59))

        self.ui.le_main.returnPressed.connect(lambda: self.on_user_input_sn_or_pallet())
        self.bridge_del_tv_sn = None
        self.bridge_del_pindex = None
        self.bridge_del_old_pallet = None

        # self.ui.labeL_in_pall_0.dragEnterEvent(self.click_on_pallet)
        self.set_unblock_interface()

        self.click_time = 0
        self.click_count = 0
        self.click_pindex = 0
        del self.cconfig

    def on_clicked_on_pallet(self, pallet_index: int):
        if self.program_job_type == JOB_TYPE.MAIN:  # Привязка
            if self.cpallet.is_pallet_chosen():  # Палет выбран

                def clear_time():
                    self.click_time = 0
                    self.click_count = 0
                    self.click_pindex = 0

                tunix = get_current_unix_time()
                if self.click_time < tunix:
                    clear_time()
                    self.click_time = tunix + 2
                    self.click_pindex = pallet_index

                if self.click_time > tunix:
                    if self.click_pindex == pallet_index:
                        self.click_count += 1
                        if self.click_count == 5:
                            clear_time()
                            pass
                        else:
                            return
                    else:
                        clear_time()
                        return
                else:
                    clear_time()
                    return

                max_places = self.cpallets_box.get_max_places()
                if 0 <= pallet_index <= max_places:
                    tv_sn = self.cpallets_box.get_tv_sn_from_pallete_index(pallet_index)
                    if tv_sn is not None:
                        chosen_pallet = self.cpallet.get_pallet_chosen()

                        self.bridge_del_tv_sn = tv_sn
                        self.bridge_del_pindex = pallet_index
                        self.bridge_del_old_pallet = chosen_pallet

                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Вы хотите исключить '{tv_sn}' из паллета '{chosen_pallet}' ?\n\n"
                                              f"Устройство будет исключено из паллета, а статус готовности паллета изменён на 'Не готов к отгрузке'!",
                                         title="Внимание!",
                                         variant_yes="Да", variant_no="Отмена", callback=self.i_im_grut)

    def i_im_grut(self, val):
        """ Удаление паллета"""
        if val.text() == "Да":
            success = False
            if self.cpallet.is_pallet_chosen():  # Палет выбран
                chosen_pallet = self.cpallet.get_pallet_chosen()
                if chosen_pallet == self.bridge_del_old_pallet:
                    pallet_index = self.bridge_del_pindex
                    tv_sn = self.cpallets_box.get_tv_sn_from_pallete_index(pallet_index)
                    if tv_sn is not None and self.bridge_del_tv_sn == tv_sn:

                        csql = CSQLQuerys()
                        try:
                            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                            if result_connect is True:
                                if csql.is_created_pallet(chosen_pallet) is True:
                                    date = csql.get_scanned_tv_date(chosen_pallet, tv_sn)
                                    if date is not False:

                                        # date
                                        try:
                                            tv_unix = (datetime.datetime.
                                                       strptime(str(date), '%Y-%m-%d %H:%M:%S.%f+03:00').
                                                       timestamp())
                                            tv_unix = int(tv_unix)

                                            global NON_DELETE_HOURS
                                            tunix = get_current_unix_time() - (NON_DELETE_HOURS * 3600)

                                            if tv_unix < tunix:
                                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                                 text=f"Не могу исключить устройство '{tv_sn}' с паллета '{chosen_pallet}'!\n\n"
                                                                      f"Нельзя исключать устройство, если с момента привязки прошло более {NON_DELETE_HOURS} часов.",
                                                                 title="Внимание!",
                                                                 variant_yes="Закрыть", variant_no="", callback=None)
                                                return

                                        except Exception as err:
                                            print(err)

                                        csql.delete_tv_on_pallet(tv_sn, chosen_pallet)
                                        csql.set_completed_status(chosen_pallet, False)

                                        # удаление
                                        self.cpallets_box.clear_field(pallet_index)

                                        empty_places = self.cpallets_box.get_pallet_empty_places()
                                        self.ccontrol_box.set_last_places(empty_places)

                                        self.bridge_del_tv_sn = None
                                        self.bridge_del_pindex = None
                                        self.bridge_del_old_pallet = None

                                        CExcelLog.print_log(chosen_pallet, f"Исключён SN: '{tv_sn}'", -1,
                                                            self.assembled_line)
                                        self.cpallet_label.set_error(4, "red", "Устройство исключено с паллета!")
                                        success = True
                                    else:
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                         text=f"Не могу исключить устройство '{tv_sn}' с паллета '{chosen_pallet}'!\n\n"
                                                              f"Устройство не привязано к этому паллету.",
                                                         title="Внимание!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)
                                        return
                        except:
                            self.send_error_message(
                                "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                                "Обратитесь к системному администратору!\n\n"
                                "Код ошибки: 'on_user_input_sn_or_pallet -> is_delete_tv'")
                            return
                        finally:
                            csql.disconnect_from_db()

                if not success:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                     text=f"Не могу исключить устройство с паллета!\n\n"
                                          f"Позовите технолога!!!",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)

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
                if is_tv_sn_valid(input_text) is True:
                    if self.cpallet.is_pattern_match(template_tv, input_text):
                        csql = CSQLQuerys()
                        try:
                            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                            if result_connect is True:
                                if csql.is_created_pallet(chosen_pallet) is False:
                                    self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
                                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                     text=f"Указанный паллет '{chosen_pallet}' не найден!\n"
                                                          f"Данные паллета сброшены!\n\n"
                                                          f"Внимание! Перескинируйте все устройства на другой паллет!!!",
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
                            # TODO Вход при первичном вводе паллета если он полный
                            if self.auto_complect is True:
                                self.cpallet_label.set_error(3, "green", "Паллет полон и автоматически закрыт!")
                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                                 text=f"Указанный паллет '{chosen_pallet}' уже сформирован полностью!\n"
                                                      f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                      f"Паллет готов к отгрузке!",
                                                 title="Успех!",
                                                 variant_yes="Закрыть", variant_no="", callback=None)

                                self.clear_current_pallet()
                                # todo Паллет обнулён из за переполнения

                                if self.set_pallet_completed_status(chosen_pallet, True) is False:
                                    print("Внимание! Ошибка проставки даты комплектности паллета. Вызов: 1")

                            else:  # автокомплект отключен
                                self.cpallet_label.set_error(2, "green", "Паллет полон и автоматически закрыт!")
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
                                            self.cpallet_label.set_error(2, "red", "Внимание!")
                                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                             text=f"Указанный серийный номер '{input_text}' найден в другом паллете '{old_pallete_code}' !\n"
                                                                  f"Позовите технолога!",
                                                             title="Внимание!",
                                                             variant_yes="Закрыть", variant_no="", callback=None)

                                            self.csn_input.set_clear_label()
                                            return

                                    result = csql.get_tv_info(input_text)
                                    if result is not False:

                                        complect_check_time = result.get(SQL_TABLE_ASSEMBLED_TV.fd_completed_scan_time,
                                                                         None)
                                        if complect_check_time is None:
                                            self.cpallet_label.set_error(2, "red", "Внимание!")
                                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                             text=f"Указанный серийный номер '{input_text}' не прошёл "
                                                                  f"проверку комплектности на упаковке !\n"
                                                                  f"Позовите технолога!",
                                                             title="Внимание!",
                                                             variant_yes="Закрыть", variant_no="", callback=None)

                                            self.csn_input.set_clear_label()
                                            return

                                        len_sn = len(input_text)
                                        sn_last = input_text[len_sn - 3:len_sn]
                                        if sn_last.find("001") == -1:  # Проверка на образец, образец везде пропустит
                                            line_fk = result.get(SQL_TABLE_ASSEMBLED_TV.fd_line_fk, None)
                                            if line_fk != self.assembled_line:
                                                self.cpallet_label.set_error(2, "red", "Внимание!")
                                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                                 text=f"Указанный серийный номер '{input_text}' был произведён на производственной линии №:{line_fk}!\n"
                                                                      f"В конфигурации программы указан №:{self.assembled_line}.\n\n"
                                                                      f"Позовите технолога!",
                                                                 title="Внимание!",
                                                                 variant_yes="Закрыть", variant_no="", callback=None)

                                                self.csn_input.set_clear_label()
                                                return

                                        tv_fk = result.get(SQL_TABLE_TV_CONFIG.fd_tv_id, None)
                                    else:
                                        self.cpallet_label.set_error(2, "red", "Внимание!")
                                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                                         text=f"Указанный серийный номер '{input_text}' не найден в числе "
                                                              f"собранных устройств!\n"
                                                              f"Позовите технолога!",
                                                         title="Внимание!",
                                                         variant_yes="Закрыть", variant_no="", callback=None)

                                        self.csn_input.set_clear_label()
                                        return

                            except:
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

                                    CExcelLog.print_log(chosen_pallet, input_text, tv_fk, self.assembled_line)

                                    # todo SN заведён

                                    if empty_places <= 0:
                                        # TODO Вход в присвоение сн паллету со ввода в ещё не полный паллет
                                        if self.auto_complect is True:
                                            self.cpallet_label.set_error(3, "green", "Паллет сформирован и автозакрыт.")
                                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                                             text=f"Указанный паллет '{chosen_pallet}' сформирован!\n"
                                                                  f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                                  f"Паллет готов к отгрузке!",
                                                             title="Успех!",
                                                             variant_yes="Закрыть", variant_no="", callback=None)

                                            if self.set_pallet_completed_status(chosen_pallet, True) is False:
                                                print("Внимание! Ошибка проставки даты комплектности паллета. Вызов: 2")

                                            self.clear_current_pallet()
                                            # todo Паллет обнулён из за переполнения
                                        else:  # автокомплект отключен
                                            self.cpallet_label.set_error(3, "green", "Паллет успешно сформирован.")
                                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                                             text=f"Указанный паллет '{chosen_pallet}' сформирован!\n"
                                                                  f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                                  f"Нажмите кнопку 'Завершить паллет', что бы закрыть выбранный паллет!",
                                                             title="Успех!",
                                                             variant_yes="Закрыть", variant_no="", callback=None)
                                            # todo Паллет набился но не обнулён, так как авто комплект отключен
                                    else:
                                        self.cpallet_label.set_error(2, "grey", f"Устройство добавлено на паллет!")
                                    return True

                                else:
                                    self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
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
                                            if self.set_pallet_completed_status(chosen_pallet, False, csql) is False:
                                                print("Внимание! Ошибка проставки даты комплектности паллета. Вызов: 3")

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
                            if self.repeat_tv_error_type == REPEAT_TV_ERROR_TYPES.WINDOW:
                                self.cpallet_label.set_error(2, "red", "Внимание!")

                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                 text=f"В паллете '{chosen_pallet}' уже есть устройство с указанным серийным "
                                                      f"номером '{input_text}' !",
                                                 title="Внимание!",
                                                 variant_yes="Закрыть", variant_no="", callback=None)
                                self.csn_input.set_clear_label()
                            else:
                                self.cpallet_label.set_error(3, "yellow", f"Повтор SN: '{input_text}'")
                                self.csn_input.set_clear_label()

                            return

                    else:
                        self.cpallet_label.set_error(2, "red", "Внимание!")
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Шаблон серийного номера устройства не совпал с указанным серийным номером! '{template_tv}' -> | '{input_text}'",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        self.csn_input.set_clear_label()
                        return
                else:
                    self.cpallet_label.set_error(2, "red", "Внимание!")
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Ошибка ввода SN устройства!\n"
                                          f"Допускается вводить только цифры и буквы латинского алфавита.",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.csn_input.set_clear_label()
                    return

            else:  # Если паллет не выбран то

                if is_pallet_text_valid(input_text) is True:
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

                                    result_open = self.load_sns_in_pallet(input_text)
                                    if isinstance(result_open, bool):
                                        if result_open is True:
                                            success_load = True
                                    elif isinstance(result_open, int):
                                        if result_open > 0:
                                            success_load = True

                                    if success_load is True:
                                        self.cpallet_label.set_error(2, "blue1", "Паллет открыт!")

                                else:  # если паллета нет - создаём

                                    if csql.create_new_pallet(input_text, self.assembled_line) is not False:
                                        if csql.is_pallet_have_any_sn(input_text) is False:
                                            success_load = True
                                            self.cpallet_label.set_error(2, "blue2", "Паллет успешно создан!")
                                        else:
                                            self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
                                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                             text=f"В новом паллете '{input_text}' обнаружены устройства "
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

                            self.csn_input.set_clear_label()
                            self.csn_input.enable_btns()
                            self.cpallet.set_pallet_chosen(input_text)
                            self.cpallets_box.set_unblock_frame()
                            if empty_places > 0:  # Места ещё есть

                                # отключил, зачем открывать при каждом открытии палета
                                # if self.set_pallet_completed_status(input_text, False) is False:
                                #     print("Внимание! Ошибка проставки даты комплектности паллета. Вызов: 5")

                                # todo Паллет заведён
                                return True
                            else:  # Мест нет
                                self.cpallet_label.set_error(2, "red", "Внимание!")
                                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                                 text=f"В паллете '{input_text}' больше нет места.\n\n"
                                                      f"Вы можете изменить конфиг, добавив дополнительные места, или "
                                                      f"закрыть паллет, нажав на кнопку 'Завершить паллет'.",
                                                 title="Внимание!",
                                                 variant_yes="Закрыть", variant_no="", callback=None)
                                # self.csn_input.set_clear_label()
                                #
                                # # сбрасываем бокс
                                # self.clear_current_pallet()
                                return True

                    else:
                        self.cpallet_label.set_error(2, "red", "Внимание!")
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        self.csn_input.set_clear_label()
                else:
                    self.cpallet_label.set_error(2, "red", "Внимание!")
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Допускается вводить только цифры и буквы латинского алфавита!\n"
                                          f"Длина SN номера паллета должна быть от 9 до 20 символов.",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.csn_input.set_clear_label()

        return False

    def set_pallet_completed_status(self, pallette_code: str, variant: bool, sql_handle: any = False):

        if sql_handle is False:
            csql = CSQLQuerys()
        else:
            csql = sql_handle
        try:
            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
            if result_connect is True:
                if csql.set_completed_status(pallette_code, variant) is True:
                    return True
        except:
            self.send_error_message(
                "Во время установки статуса комплектности прозошла ошибка.\n"
                "Обратитесь к системному администратору!\n\n"
                "Код ошибки: 'load_job_mode -> auto_complect -> set_completed_status'")
        finally:
            csql.disconnect_from_db()
        return False

    def load_info_mode(self, input_text, template_pallet):
        # if self.cpallet.is_pattern_match(template_pallet, input_text):
        if is_pallet_text_valid(input_text) is True:
            # if self.cpallet.get_pallet_chosen() != input_text: вдруг переобновить надо
            success_load = False
            result_open = self.load_sns_in_pallet(input_text)
            if isinstance(result_open, bool):
                if result_open is True:
                    success_load = True
            elif isinstance(result_open, int):
                if result_open > 0:
                    success_load = True

            if success_load is True:
                pallet_status = self.get_pallete_status(input_text)
                self.cpallet.set_pallet_chosen(input_text)

                if isinstance(result_open, int):
                    self.ccontrol_box.set_count_in_pallet(result_open)
                else:
                    self.ccontrol_box.set_count_in_pallet(0)

                self.ccontrol_box.set_pallet_status(pallet_status)

                self.cpallet_label.set_name(input_text)
                self.csn_input.set_clear_label()
                self.cpallet_label.set_error(2, "grey",
                                             "Паллет открыт для просмотра!")
                return True
        else:
            self.cpallet_label.set_error(2, "red", "Внимание!")
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"Допускается вводить только цифры и буквы латинского алфавита!\n"
                                  f"Длина SN номера паллета должна быть от 9 до 20 символов!",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            self.csn_input.set_clear_label()
        # else:
        #     self.cpallet_label.set_error(2, "red", "Внимание!")
        #     send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
        #                      text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
        #                      title="Внимание!",
        #                      variant_yes="Закрыть", variant_no="", callback=None)
        #     self.csn_input.set_clear_label()

        return False

    def load_sns_in_pallet(self, pallette_code: str) -> bool | int:

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
                            return count

                    else:
                        if self.program_job_type == JOB_TYPE.INFO:
                            self.cpallet_label.set_error(2, "red", "Внимание!")
                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                             text=f"Указанный паллет '{pallette_code}' найден, но не имеет привязанных устройств!",
                                             title="Внимание!",
                                             variant_yes="Закрыть", variant_no="", callback=None)
                        else:
                            # Даём так как можно открыть пустой паллет и заполнять его
                            return True
                else:

                    if self.program_job_type == JOB_TYPE.INFO:
                        self.cpallet_label.set_error(2, "red", "Внимание!")
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                         text=f"Указанный паллет '{pallette_code}' не найден!",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        return False
                    else:
                        return True
        except:
            self.send_error_message(
                "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                "Обратитесь к системному администратору!\n\n"
                "Код ошибки: 'load_sns_in_pallet -> get_sn_data'")
        finally:
            csql.disconnect_from_db()

        return False

    def get_pallete_status(self, pallette_code: str) -> bool:
        """
        Сформирован или нет
        :param pallette_code:
        :return:
        """

        csql = CSQLQuerys()
        try:
            result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
            if result_connect is True:
                status = csql.is_pallette_completed(pallette_code)
                if status is True:
                    return True
        except:
            self.send_error_message(
                "Во время получения статуса паллета возникла ошибка.\n"
                "Обратитесь к системному администратору!\n\n"
                "Код ошибки: 'pallet_info -> get_pallete_status'")
        finally:
            csql.disconnect_from_db()

        return False

    def on_user_pressed_pallet_complete(self, variant: str):
        """Слот на кнопки создать и отменить паллет
        По сути одно и тоже. Только в отмене, если палет пустой, спросит отменить ли,
        а в создании не даст отменить написав что нет телеков"""

        if AntiFlood.is_flood() is True:
            return

        if not self.cpallet.is_pallet_chosen():
            self.cpallet_label.set_error(2, "yellow", "Внимание!")
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
        current_count_in_pallet = self.cpallets_box.get_closest_places()
        # print(current_count_in_pallet)

        if max_places == 0:
            self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"С паллетом '{pallette_code}' возникла ошибка.",
                             title="Внимание! Позовите технолога!!!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            return
        if empty_places == max_places:
            if variant == "cancel":
                self.cpallet_label.set_error(2, "yellow", "Внимание!")
                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                 text=f"На паллете '{pallette_code}' нет устройств.\n\n"
                                      f"Вы уверены, что хотите закончить формирование ?\n"
                                      f"Продолжить формирование можно в любой момент, просто введите номер этого паллета.",
                                 title="Внимание!",
                                 variant_yes="Да", variant_no="Нет",
                                 callback=self.on_user_clicked_variant_on_btn_cancel)

            elif variant == "success":
                self.cpallet_label.set_error(2, "yellow", "Внимание!")
                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                 text=f"На паллете '{pallette_code}' нет устройств.",
                                 title="Внимание!",
                                 variant_yes="Закрыть", variant_no="", callback=None)
            return

        if variant == "success":
            # это заведомо неверно так как паллет задумывалось закрывать вручную без технолога,
            # но Саша попросил что бы технолог контролировал!
            # Поэтому только автозакрытие!

            # То что Саша насоветовал
            # self.cpallet_label.set_error(2, "yellow", "Внимание!")
            # send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
            #                  text=(f"Вы уверены, что хотите закончить формирование паллета '{pallette_code}' ?\n\n"
            #                        f"Паллет ещё не заполнен!\n\n"
            #                        f"Для принудительного закрытия позовите технолога, для "
            #                        f"изменения количества устройств в файле конфигурации."),
            #                  title="Внимание!",
            #                  variant_yes="Закрыть", variant_no="",
            #                  callback=None)

            # Мой изначальный код:
            # если меньше чем в конфиге на паллете то пусть технолога зовут
            if current_count_in_pallet == max_places:

                self.cpallet_label.set_error(2, "yellow", "Внимание!")
                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                 text=(f"Вы уверены, что хотите закончить формирование паллета '{pallette_code}' ?\n\n"
                                       f"Продолжить формирование можно в любой момент, просто введите номер этого паллета.\n\n"
                                       f"Статус для паллета будет установлен на 'Сформирован'."),
                                 title="Внимание!",
                                 variant_yes="Да", variant_no="Нет",
                                 callback=self.on_user_clicked_variant_btn_pallette_complete)
            else:

                self.cpallet_label.set_error(2, "yellow", "Внимание!")
                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                 text=(
                                     f"Вы не можете завершить паллет '{pallette_code}', так как не все устройства отсканированы.\n\n"
                                     f"Позовите технолога для завершения паллета с текущим количеством устройств."),
                                 title="Внимание!",
                                 variant_yes="Закрыть", variant_no="",
                                 callback=None)

        elif variant == "cancel":
            self.cpallet_label.set_error(2, "yellow", "Внимание!")
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=(f"Вы уверены, что хотите отменить формирование паллета '{pallette_code}' ?\n\n"
                                   f"Продолжить формирование можно в любой момент, просто введите номер этого паллета."),
                             title="Внимание!",
                             variant_yes="Да", variant_no="Нет",
                             callback=self.on_user_clicked_variant_on_btn_cancel)

        return True

    def on_user_clicked_variant_on_btn_cancel(self, val):
        if val.text() == "Да":
            pallette_code = self.cpallet.get_pallet_chosen()

            self.csn_input.set_clear_label()
            self.clear_current_pallet()

            self.cpallet_label.set_error(3, "yellow", f"Паллет '{pallette_code}' отменён!")
        else:
            pass

    def on_user_clicked_variant_btn_pallette_complete(self, val):
        if val.text() == "Да":

            pallette_code = self.cpallet.get_pallet_chosen()

            if len(pallette_code) > 0:
                if self.set_pallet_completed_status(pallette_code, True) is False:
                    print("Внимание! Ошибка проставки даты комплектности паллета. Вызов: 4")

            self.csn_input.set_clear_label()
            self.clear_current_pallet()
            self.cpallet_label.set_error(3, "green", f"Паллет '{pallette_code}' сформирован!")

        else:
            pass

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
        self.cpallet_label.set_error(2, "red", "Внимание! Возникла ошибка.")
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
        self.cpallets_box.set_block_frame()

    def set_block_interface(self):
        self.ui.centralwidget.setDisabled(True)

    def set_unblock_interface(self):
        self.ui.centralwidget.setDisabled(False)

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
