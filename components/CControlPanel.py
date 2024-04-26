from ui.interface import Ui_MainWindow


class CControlPanel:
    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface

    def set_max_places(self, places: int):
        self.interface.label_all_places.setText(f"Всего мест: {places} (Конфиг)")

    def set_last_places(self, places: int):
        self.interface.label_last_places.setText(f"Осталось мест: {places}")

    def disable_place_info(self):
        self.interface.places_frame.setEnabled(False)  # не работает для лайаутов
