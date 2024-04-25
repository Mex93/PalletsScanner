from ui.interface import Ui_MainWindow

from config_parser.CConfig import MAX_PALLET_PLACES


class CPalletInfoBOX:
    empty_place_text = '-'

    def __init__(self, interface: Ui_MainWindow):
        self.interface = interface
        self.max_place = 0
        self.blocked_frame = True

        self.labels = [
            interface.labeL_in_pall_0,
            interface.labeL_in_pall_1,
            interface.labeL_in_pall_2,
            interface.labeL_in_pall_3,
            interface.labeL_in_pall_4,
            interface.labeL_in_pall_5,
            interface.labeL_in_pall_6,
            interface.labeL_in_pall_7,
            interface.labeL_in_pall_8,
            interface.labeL_in_pall_9,
            interface.labeL_in_pall_10,
            interface.labeL_in_pall_11,
            interface.labeL_in_pall_12,
            interface.labeL_in_pall_13,
            interface.labeL_in_pall_14,
            interface.labeL_in_pall_15,
            interface.labeL_in_pall_16,
            interface.labeL_in_pall_17,
            interface.labeL_in_pall_18,
            interface.labeL_in_pall_19,
            interface.labeL_in_pall_20,
            interface.labeL_in_pall_21,
            interface.labeL_in_pall_22,
            interface.labeL_in_pall_23,
            interface.labeL_in_pall_24,
            interface.labeL_in_pall_25,
            interface.labeL_in_pall_26,
            interface.labeL_in_pall_27,
            interface.labeL_in_pall_28,
            interface.labeL_in_pall_29,
            interface.labeL_in_pall_30,
            interface.labeL_in_pall_31,
            interface.labeL_in_pall_32,
            interface.labeL_in_pall_33,
            interface.labeL_in_pall_34,
            interface.labeL_in_pall_35,
        ]

        for index in range(0, MAX_PALLET_PLACES):
            self.labels[index].setText(self.empty_place_text)

        self.sn_list = None

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

        # self.sn_list = []
        # for index in range(0,  self.max_place):
        #     self.sn_list.append("Место свободно")
        #     self.labels[index].setStyleSheet(u"color:blue")
        #     self.labels[index].setText("Место свободно")
        #
        # for index in range(self.max_place,  MAX_PALLET_PLACES):
        #     self.sn_list.append("---")
        #     self.labels[index].setStyleSheet(u"color:gray")
        #     self.labels[index].setText("----")

    def set_sn_in_pallet(self, sn: str) -> bool:
        for index in range(0, self.max_place):
            if isinstance(self.sn_list[index], int) and self.sn_list[index] == -1:
                self.labels[index].setStyleSheet(u"color:blue")
                self.labels[index].setText(sn)
                self.sn_list[index] = sn
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
