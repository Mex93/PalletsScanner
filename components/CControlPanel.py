from ui.interface import Ui_MainWindow


class CControlPanel:
    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface

    def set_max_places(self, places: int):
        self.interface.label_all_places.setText(f"Всего мест: {places} штук (Конфиг)")

    def set_count_in_pallet(self, places: int):
        self.interface.label_all_places.setText(f"Устройств на паллете: {places} штук")

    def set_clear_last_place(self):
        self.interface.label_last_places.setText(f"Осталось мест: - штук")

    def set_pallet_status(self, status: bool):
        if status is True:
            self.interface.label_last_places.setText("Статус паллета: сформирован!")
            self.interface.label_last_places.setStyleSheet(u"color: green")
        else:
            self.interface.label_last_places.setText("Статус паллета: не сформирован!")
            self.interface.label_last_places.setStyleSheet(u"color: red")

    def set_last_places(self, places: int):
        self.interface.label_last_places.setText(f"Осталось мест: {places} штук")

    def disable_place_info(self):
        self.interface.places_frame.setEnabled(False)  # не работает для лайаутов
