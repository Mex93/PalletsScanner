from ui.interface import Ui_MainWindow

from sql.CSQLQuerys import CSQLQuerys
from sql.enums import CONNECT_DB_TYPE


class CControlPanel:
    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface

    def set_max_pallets(self, max_pallets: int):
        self.interface.label_all_pallets.setText(f"Всего паллетов согласно шаблону: {max_pallets} шт")

    def update_max_pallets_field(self, pallet_template, sql_handle: any = False):

        sql_new = False
        if sql_handle is False:
            csql = CSQLQuerys()
            sql_new = True
        else:
            csql = sql_handle
        try:
            if sql_new is True:
                result_connect = csql.connect_to_db(CONNECT_DB_TYPE.LINE)
                if result_connect is False:
                    return False
            pallet_template = pallet_template.replace("*", "%")
            max_pallets = csql.get_max_pallets(pallet_template)
            if isinstance(max_pallets, int):
                self.set_max_pallets(max_pallets)
            else:
                self.set_max_pallets(-1)
        except:
            self.set_max_pallets(0)
        finally:
            if sql_new is True:
                csql.disconnect_from_db()

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
