from ui.interface import Ui_MainWindow

from config_parser.CConfig import MAX_PALLET_PLACES


class CPalletLabel:
    current_pallet = ""

    def __init__(self, interface: Ui_MainWindow):
        self.label = interface.label_pallet_name
        self.label_default_text = ""
        self.current_pallet = ""

    def set_name(self, string: str):
        self.label.setText(string)

    def set_default_text(self, string: str):
        self.label_default_text = string

    def set_unlock_color(self):
        self.label.setStyleSheet(u"color:red")

    def clear(self):
        self.set_name(self.label_default_text)
        self.label.setStyleSheet(u"color:red")


