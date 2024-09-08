import random
import clr
import sys

from enums import BARCODE_TYPE

MAX_PLACES_IN_BARCODE = 48


class CPrinter:
    def __init__(self, printer_name: str):
        self.__printer_name = printer_name
        # Добавьте путь к вашей DLL
        sys.path.append(r'../LabelPrinterLibrary.dll')
        # Загрузите вашу DLL:
        clr.AddReference('LabelPrinterLibrary')

        # sn = "2409K14F2K43UH90202758"
        # for index in range(6):
        #     if random.randint(0, 2) == 0:
        #         sn += "S"
        #     else:
        #         sn += "2"
        # print(sn)
        # tvlist = list(sn for item in range(12))
        # print(tvlist)
        #
        # RESULT = self.send_print_label("P092401K43UH90215KV00045", tvlist, "KVANT", "TV Tricolor K43UH902 FL")
        # print("P092401K43UH90215KV00045", tvlist, "KVANT", "TV Tricolor K43UH902 FL")
        # print(RESULT)

    def __print_label(self, barcode_text):
        from LabelPrinterLibrary import LabelPrinter
        result = LabelPrinter.PrintBarcode(self.__printer_name, barcode_text)
        return result

    @staticmethod
    def get_barcode_name_from_barcode_type(barcode_type: BARCODE_TYPE) -> str | bool:
        match barcode_type:
            case BARCODE_TYPE.BAR_4:
                return "barcode_template_4"
            case BARCODE_TYPE.BAR_8:
                return "barcode_template_8"
            case BARCODE_TYPE.BAR_12:
                return "barcode_template_12"
            case BARCODE_TYPE.BAR_16:
                return "barcode_template_16"
            case BARCODE_TYPE.BAR_24:
                return "barcode_template_24"
            case BARCODE_TYPE.BAR_32:
                return "barcode_template_32"
            case BARCODE_TYPE.BAR_48:
                return "barcode_template_48"
            case _:
                return False

    @staticmethod
    def get_barcode_type_from_tv_count(tv_count: int) -> BARCODE_TYPE | bool:
        if 1 <= tv_count <= 4:
            return BARCODE_TYPE.BAR_4
        elif 5 <= tv_count <= 8:
            return BARCODE_TYPE.BAR_8
        elif 9 <= tv_count <= 12:
            return BARCODE_TYPE.BAR_12
        elif 13 <= tv_count <= 16:
            return BARCODE_TYPE.BAR_16
        elif 17 <= tv_count <= 24:
            return BARCODE_TYPE.BAR_24
        elif 25 <= tv_count <= 32:
            return BARCODE_TYPE.BAR_32
        elif 33 <= tv_count <= 48:
            return BARCODE_TYPE.BAR_48
        else:
            return False

    def send_print_easy_label(self, pallet_sn: str, tv_model_name: str) -> bool:
        with open(f'barcodes/barcode_template_standart.txt', 'r') as file:
            ezpl_data = file.read()
            if len(ezpl_data) == 0:
                return False
            dots_start_tv_name = (800 - (22 * len(tv_model_name))) / 2
            dots_start_qr = (800 - (22 * len(pallet_sn))) / 2
            ezpl_data = ezpl_data.replace("TV_SHIFT_VERTICAL_COUNT", str(int(dots_start_tv_name)))
            ezpl_data = ezpl_data.replace("QR_SHIFT_VERTICAL_COUNT", str(int(dots_start_qr)))
            ezpl_data = ezpl_data.replace("TV_NAME", tv_model_name)
            ezpl_data = ezpl_data.replace("PALLET_CODE", pallet_sn)
            self.__print_label(ezpl_data)
            print("PRINT")
            # print(ezpl_data)
            return True

    def send_print_label_tricolor(self, pallet_sn: str, tv_list: list, assembled_tm: str, tv_model_name: str) -> bool:
        count = len(tv_list)
        if count > 0:
            barcode_template_type = self.get_barcode_type_from_tv_count(count)
            if isinstance(barcode_template_type, BARCODE_TYPE):
                barcode_template_name = self.get_barcode_name_from_barcode_type(barcode_template_type)
                if isinstance(barcode_template_name, str):
                    with open(f'barcodes/{barcode_template_name}.txt', 'r') as file:
                        ezpl_data = file.read()
                        if len(ezpl_data) == 0:
                            return False

                        ezpl_data = ezpl_data.replace("TV_COUNT", f"{str(count)} шт")
                        ezpl_data = ezpl_data.replace("TV_NAME", tv_model_name)
                        ezpl_data = ezpl_data.replace("KVANT", assembled_tm)
                        count_sym = 0
                        for index, tv in enumerate(tv_list, 0):
                            clen = len(tv)
                            if not clen:
                                continue
                            count_sym += clen
                            ezpl_data = ezpl_data.replace(f"TPLACE_{index:02}", tv)
                            ezpl_data = ezpl_data.replace(f"QPLACE_{index:02}", tv)

                        # удаление лишних
                        for index in range(0, MAX_PLACES_IN_BARCODE):

                            if ezpl_data.find(f"TPLACE_{index:02}") != -1:
                                ezpl_data = ezpl_data.replace(f"TPLACE_{index:02}", "")

                            if ezpl_data.find(f"QPLACE_{index:02}") != -1:
                                ezpl_data = ezpl_data.replace(f"QPLACE_{index:02}", "")

                        ezpl_data = ezpl_data.replace("QPALLET_CODE_COUNT_SYM", str(len(pallet_sn)))
                        ezpl_data = ezpl_data.replace(f"COUNT_SYM", str(count_sym + count))
                        ezpl_data = ezpl_data.replace("PALLET_CODE", pallet_sn)
                        ezpl_data += '\n'
                        self.__print_label(ezpl_data)
                        print("PRINT")
                        # print(ezpl_data)
                        return True
        return False
