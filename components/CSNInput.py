from ui.interface import Ui_MainWindow


class CSNinput:

    def __init__(self, interface: Ui_MainWindow):
        self.input_field = interface.le_main

    def get_current_text(self):
        return self.input_field.text()

    def set_clear_label(self):
        self.input_field.clear()

