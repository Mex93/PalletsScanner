from ui.interface import Ui_MainWindow


class CSNinput:

    def __init__(self, interface: Ui_MainWindow):
        self.input_field = interface.le_main
        self.interface = interface

    def get_current_text(self):
        return self.input_field.text()

    def set_clear_label(self):
        self.input_field.clear()

    def disabled_btns(self):
        self.interface.pushButton_set_cancel.setEnabled(False)
        self.interface.pushButton_set_complete.setEnabled(False)

    def enable_btns(self):
        self.interface.pushButton_set_cancel.setEnabled(True)
        self.interface.pushButton_set_complete.setEnabled(True)
