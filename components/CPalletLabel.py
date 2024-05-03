from ui.interface import Ui_MainWindow
import threading
from config_parser.CConfig import MAX_PALLET_PLACES


class CPalletLabel:
    timer = None

    def __init__(self, interface: Ui_MainWindow):
        self.label = interface.label_pallet_name
        self.label_default_text = ""
        self.selected_pallet = ""

    def set_name(self, string: str):
        if self.timer is None:
            self.label.setText(string)
        self.selected_pallet = string

    def set_name_error(self):
        self.label.setText(self.selected_pallet)

    def set_default_text(self, string: str):
        self.label_default_text = string

    def clear(self):
        self.set_name(self.label_default_text)
        self.set_default_color()

    def set_error(self, time_sec: int, color: str, text: str):
        if len(text) > 0 and time_sec > 0 and len(color) > 0:
            self.label.setText(text)
            if color == "red":
                self.label.setStyleSheet(u"background-color:red")
            elif color == "green":
                self.label.setStyleSheet(u"background-color:lightgreen")
            elif color == "blue1":
                self.label.setStyleSheet(u"background-color:lightblue")
            elif color == "blue2":
                self.label.setStyleSheet(u"background-color:teal")
            elif color == "grey":
                self.label.setStyleSheet(u"background-color:grey")
            else:
                self.label.setStyleSheet(u"background-color:yellow")

            self.clear_error_time()
            self.timer = threading.Timer(time_sec, lambda: self.on_stop_error())
            self.timer.start()

    def set_default_color(self):
        self.label.setStyleSheet(u"background-color:none")

    @classmethod
    def clear_error_time(cls):
        if cls.timer is not None:
            cls.timer.cancel()
            cls.timer = None

    def on_stop_error(self):
        self.timer = None
        self.set_default_color()
        self.set_name_error()

    def stop_error(self):
        if self.timer is not None:
            self.clear_error_time()
            self.set_name_error()
