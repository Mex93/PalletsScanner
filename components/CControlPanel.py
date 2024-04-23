from ui.interface import Ui_MainWindow


class CControlPanel:
    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface

    def set_max_places(self, places: int):
        self.interface.label_all_places.setText("Всего мест: " + str(places))

    def set_last_places(self, places: int):
        self.interface.label_last_places.setText("Осталось мест: " + str(places))
