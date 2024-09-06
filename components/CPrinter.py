import random

import clr
import sys
import random
MAX_PLACES_IN_BARCODE = 48

class CPrinter:
    def __init__(self, printer_name: str):
        self.__printer_name = printer_name
        # Добавьте путь к вашей DLL
        sys.path.append(r'../LabelPrinterLibrary.dll')
        # Загрузите вашу DLL:
        clr.AddReference('LabelPrinterLibrary')

        sn = ""
        for index in range(24):
            if random.randint(0, 2) == 0:
                sn += "S"
            else:
                sn += "2"
        print(sn)
        tvlist = list(sn for item in range(12))
        print(tvlist)

        RESULT = self.send_print_label("P092401K43UH90215KV00045", tvlist, "KVANT", "TV Tricolor K43UH902 FL")
        print("P092401K43UH90215KV00045", tvlist, "KVANT", "TV Tricolor K43UH902 FL")
        print(RESULT)



    def __print_label(self, barcode_text):
        from LabelPrinterLibrary import LabelPrinter
        result = LabelPrinter.PrintBarcode(self.__printer_name, barcode_text)
        return result

    @staticmethod
    def get_barcode_name_from_tv_count(tv_count: int) -> str | bool:
        if 1 <= tv_count <= 4:
            return "barcode_template_4"
        elif 5 <= tv_count <= 8:
            return "barcode_template_8"
        elif 9 <= tv_count <= 12:
            return "barcode_template_12"
        elif 13 <= tv_count <= 16:
            return "barcode_template_16"
        elif 17 <= tv_count <= 24:
            return "barcode_template_24"
        elif 25 <= tv_count <= 32:
            return "barcode_template_32"
        elif 33 <= tv_count <= 48:
            return "barcode_template_48"
        else:
            return False

    def send_print_label(self, pallet_sn: str, tv_list: list, assembled_tm: str, tv_model_name: str) -> bool:
        # if isinstance((assembled_tm, tv_model_name), str) and isinstance(tv_list, list):
        #
        #     if len(pallet_sn) and len(assembled_tm) and len(tv_model_name):

        count = len(tv_list)

        barcode_template_name = self.get_barcode_name_from_tv_count(count)
        if isinstance(barcode_template_name, str):
            with open(f'barcodes/{barcode_template_name}.txt', 'r') as file:
                ezpl_data = file.read()
                if len(ezpl_data) == 0:
                    return False

                ezpl_data = ezpl_data.replace("PALLET_CODE", pallet_sn)
                ezpl_data = ezpl_data.replace("TV_COUNT", f"{str(count)} шт")
                ezpl_data = ezpl_data.replace("TV_NAME", tv_model_name)
                ezpl_data = ezpl_data.replace("KVANT", assembled_tm)
                count_sym = 0
                for index, tv in enumerate(tv_list, 0):
                    print(index)
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

                ezpl_data = ezpl_data.replace(f"COUNT_SYM", str(count_sym + count))
                ezpl_data += '\n'
                self.__print_label(ezpl_data)
                print("FINAL")
                print(ezpl_data)
                return True



            # нельзя впереди этикетки что бы были пробелы!!!!!!
            # в документе должен быть пробел в самом конце после E
        #return False
