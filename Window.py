from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QFontDatabase

import sys
import threading
from openpyxl import Workbook
from openpyxl.utils.cell import get_column_interval
from openpyxl.styles import (
    Alignment, Font
)

from common_func import send_message_box, SMBOX_ICON_TYPE
from ui.interface import Ui_MainWindow

from config_parser.CConfig import CConfig, MAX_PALLET_PLACES

from components.CPalletInfoBox import CPalletInfoBOX
from components.CPalletLabel import CPalletLabel
from components.CControlPanel import CControlPanel

current_pallet = None


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"  # Менять при каждом обновлении любой из подпрограмм

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Сканирование паллетов TCL ООО Квант 2024 v{self.__base_program_version}')

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

        # classes

        max_places_in_pallets = self.cconfig.get_pallet_max_places()
        self.cpallets_box = CPalletInfoBOX(self.ui)
        self.cpallets_box.set_max_place(max_places_in_pallets)
        self.cpallets_box.set_block_frame()

        self.cpallet_label = CPalletLabel(self.ui)
        self.cpallet_label.set_template(self.cconfig.get_pallet_template())
        self.cpallet_label.clear()

        self.ccontrol_box = CControlPanel(self.ui)
        self.ccontrol_box.set_max_places(0)
        self.ccontrol_box.set_last_places(0)

        # slots
        self.ui.pushButton_info.clicked.connect(lambda: self.on_user_pressed_info_btn)
        self.ui.pushButton_set_cancel.clicked.connect(lambda: self.on_user_pressed_pallet_cancel)
        self.ui.pushButton_set_complete.clicked.connect(lambda: self.on_user_pressed_pallet_complete)

    def on_user_pressed_pallet_complete(self):
        pass

    def on_user_pressed_pallet_cancel(self):
        pass

    def on_user_pressed_info_btn(self):
        pass

    @staticmethod
    def set_close():
        sys.exit()
