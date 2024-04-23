from ui.interface import Ui_MainWindow

from config_parser.CConfig import MAX_PALLET_PLACES


class CPalletLabel:

    def __init__(self, interface: Ui_MainWindow):
        self.label = interface.label_pallet_name
        self.pallet_template = ""

    def set_name(self, string: str):
        self.label.setText(string)

    def set_template(self, string: str):
        self.pallet_template = string

    def set_unlock_color(self):
        self.label.setStyleSheet(u"color:red")

    def clear(self):
        self.set_name(self.pallet_template)
        self.label.setStyleSheet(u"color:red")
