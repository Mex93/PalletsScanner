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
from sql.sql_data import SQL_PALLET_SCANNED


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

        # classes

        max_places_in_pallets = self.cconfig.get_pallet_max_places()
        self.cpallets_box = CPalletInfoBOX(self.ui)
        self.cpallets_box.set_max_place(max_places_in_pallets)
        self.cpallets_box.set_block_frame()

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
                                                 text=f"Ранее указанный паллет '{chosen_pallet}' не найден!\n"
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
                    finally:
                        csql.disconnect_from_db()

                    #  Паттерн совпал с заданным
                    empty_places = self.cpallets_box.get_pallet_empty_places()
                    max_places = self.cpallets_box.get_max_places()

                    if empty_places <= 0:
                        send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                         text=f"Ошибка работы программы!!! У паллета {chosen_pallet} почему то свободно 0 мест!\n"
                                              f"Данные паллета сброшены!\n\n"
                                              f"Внимание! Перескинируйте все телевизоры на другой паллет!!!",
                                         title="Внимание!",
                                         variant_yes="Закрыть", variant_no="", callback=None)
                        self.clear_current_pallet()
                        return


                    # todo Проверка на наличие копии в паллете
                    # todo проверка на наличие этого телика в другом паллете с теликами
                    # todo проверка наличия созданого в assembled телека и его прохождение через станцию проверка комплектности (по дате)

                    if self.cpallets_box.set_sn_in_pallet(input_text) is True:
                        empty_places -= 1
                        self.ccontrol_box.set_last_places(empty_places)
                        # todo SN заведён
                        if empty_places <= 0:
                            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_INFO,
                                             text=f"Указанный паллет '{chosen_pallet}' сформирован!\n"
                                                  f"Помещено: {self.cpallets_box.get_closest_places()} штук\n\n"
                                                  f"Паллет готов к отгрузке!",
                                             title="Успех!",
                                             variant_yes="Закрыть", variant_no="", callback=None)

                            self.clear_current_pallet()
                            self.cpallets_box.clear_box()
                            self.ccontrol_box.set_last_places(0)
                            self.ccontrol_box.set_max_places(0)
                            # todo Паллет обнулён из за переполнения
                            return

                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Шаблон серийного номера телевизора не совпал с указанным серийным номером! '{template_tv}' ->| '{input_text}'",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.cpallet_label.clear()
                    return
            else:  # Первым пропикаем паллет

                if self.cpallet.is_pattern_match(template_pallet, input_text):

                    success_load = False
                    csql = CSQLQuerys()
                    try:
                        result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                        if result_connect is True:
                            if csql.is_created_pallet(input_text) is True:
                                if self.load_sns_in_pallet(input_text) is True:
                                    success_load = True

                    except Exception:
                        self.send_error_message(
                            "Во время получения данных списка устройств на паллете возникла ошибка.\n"
                            "Обратитесь к системному администратору!\n\n"
                            "Код ошибки: 'on_user_input_sn_or_pallet -> get_info_data'")
                    finally:
                        csql.disconnect_from_db()

                    if success_load is True:

                        empty_places = self.cpallets_box.get_pallet_empty_places()
                        max_places = self.cpallets_box.get_max_places()

                        self.ccontrol_box.set_last_places(empty_places)
                        self.ccontrol_box.set_max_places(max_places)

                        self.cpallet.set_pallet_chosen(input_text)
                        self.cpallet_label.set_name(input_text)
                        self.cpallet_label.clear()
                        self.csn_input.enable_btns()
                        # todo Паллет заведён
                        return True
                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.cpallet_label.clear()
        return False

    def load_info_mode(self, input_text, template_pallet):
        print("gwrfgwer")
        if self.cpallet.is_pattern_match(template_pallet, input_text):

            if self.cpallet.get_pallet_chosen() != input_text:

                if self.load_sns_in_pallet(input_text) is True:
                    self.cpallet.set_pallet_chosen(input_text)
                    self.cpallet_label.set_name(input_text)
                    self.cpallet_label.clear()
                    return True

            else:
                pass
                # ничего нет так как палет указан тот же
        else:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                             text=f"Шаблон паллета не совпал с указанным номером! '{template_pallet}' ->| '{input_text}'",
                             title="Внимание!",
                             variant_yes="Закрыть", variant_no="", callback=None)
            self.cpallet_label.clear()

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
            return

        if self.program_job_type == JOB_TYPE.INFO:
            return

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
        self.cpallet_label.clear()

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
