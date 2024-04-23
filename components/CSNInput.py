from ui.interface import Ui_MainWindow


class CSNinput:

    def __init__(self, interface: Ui_MainWindow):
        self.input_field = interface.le_main
        self.pallet_template = ""

    def set_pallet_template(self, string: str):
        self.pallet_template = string

    def is_pallet(self, text: str) -> bool:
        template_len = len(self.pallet_template)
        text_len = len(text)
        if text_len == template_len:
            for index, sym in enumerate(self.pallet_template):
                if text[index] != sym:
                    return False
            return True

        return False
