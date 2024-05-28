from ui.interface import Ui_MainWindow

from config_parser.CConfig import MAX_PALLET_PLACES


class CPalletInfoBOX:
    empty_place_text = '-'

    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface
        self.max_place = 0
        self.blocked_frame = True

        self.labels = [
            interface.pushButton_field_0,
            interface.pushButton_field_1,
            interface.pushButton_field_2,
            interface.pushButton_field_3,
            interface.pushButton_field_4,
            interface.pushButton_field_5,
            interface.pushButton_field_6,
            interface.pushButton_field_7,
            interface.pushButton_field_8,
            interface.pushButton_field_9,
            interface.pushButton_field_10,
            interface.pushButton_field_11,
            interface.pushButton_field_12,
            interface.pushButton_field_13,
            interface.pushButton_field_14,
            interface.pushButton_field_15,
            interface.pushButton_field_16,
            interface.pushButton_field_17,
            interface.pushButton_field_18,
            interface.pushButton_field_19,
            interface.pushButton_field_20,
            interface.pushButton_field_21,
            interface.pushButton_field_22,
            interface.pushButton_field_23,
            interface.pushButton_field_24,
            interface.pushButton_field_25,
            interface.pushButton_field_26,
            interface.pushButton_field_27,
            interface.pushButton_field_28,
            interface.pushButton_field_29,
            interface.pushButton_field_30,
            interface.pushButton_field_31,
            interface.pushButton_field_32,
            interface.pushButton_field_33,
            interface.pushButton_field_34,
            interface.pushButton_field_35,
            interface.pushButton_field_36,
            interface.pushButton_field_37,
            interface.pushButton_field_38,
            interface.pushButton_field_39,
            interface.pushButton_field_40,
            interface.pushButton_field_41,
            interface.pushButton_field_42,
            interface.pushButton_field_43,
            interface.pushButton_field_44,
            interface.pushButton_field_45,
            interface.pushButton_field_46,
            interface.pushButton_field_47,
            interface.pushButton_field_48,
            interface.pushButton_field_49,
            interface.pushButton_field_50,
            interface.pushButton_field_51,
            interface.pushButton_field_52,
            interface.pushButton_field_53,
            interface.pushButton_field_54,
            interface.pushButton_field_55,
            interface.pushButton_field_56,
            interface.pushButton_field_57,
            interface.pushButton_field_58,
            interface.pushButton_field_59
        ]

        self.sn_list = []

        for index in range(0, MAX_PALLET_PLACES):
            self.labels[index].setText(self.empty_place_text)

    def set_max_place(self, max_place: int):
        self.max_place = max_place
        self.clear_box()

    def get_max_places(self):
        return self.max_place

    def clear_box(self):
        self.sn_list = []
        for index in range(0, MAX_PALLET_PLACES):
            self.sn_list.append(-1)
            self.labels[index].setStyleSheet(u"color:gray")
            self.labels[index].setText(self.empty_place_text)

    def set_sn_in_pallet(self, sn: str) -> bool:
        for index in range(0, MAX_PALLET_PLACES):
            if isinstance(self.sn_list[index], int) and self.sn_list[index] == -1:
                self.labels[index].setStyleSheet(u"color:blue")
                self.labels[index].setText(sn)
                self.sn_list[index] = sn
                return True
        return False

    def get_closest_places(self):
        count = 0
        for index in range(0, self.max_place):
            if isinstance(self.sn_list[index], str):
                count += 1
        return count

    def get_place_index_from_tv_sn(self, tv_sn: str) -> int:
        """Проверка на наличие в паллете"""
        for index in range(0, self.max_place):
            if isinstance(self.sn_list[index], str):
                if self.sn_list[index] == tv_sn:
                    return index
        return -1

    def get_tv_sn_from_pallete_index(self, pindex: int) -> str | None:
        """Получить серийник телека зная индекс"""

        if isinstance(self.sn_list[pindex], str):
            return self.sn_list[pindex]

        return None


    def clear_field(self, place_index: int) -> bool:
        """Обнуление места"""
        if isinstance(self.sn_list[place_index], str):
            self.sn_list[place_index] = -1
            self.labels[place_index].setStyleSheet(u"color:gray")
            self.labels[place_index].setText(self.empty_place_text)
            return True
        return False

    def get_pallet_empty_places(self) -> int:
        count = 0
        for index in range(0, self.max_place):
            if isinstance(self.sn_list[index], int) and self.sn_list[index] == -1:
                count += 1
        return count

    def set_block_frame(self):
        self.interface.gridLayout_inpallets_table.setEnabled(False)
        self.blocked_frame = True

    def set_unblock_frame(self):
        self.interface.gridLayout_inpallets_table.setEnabled(True)
        self.blocked_frame = False
