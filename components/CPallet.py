class CPallet:
    current_chosen_palet = ""

    def __init__(self):
        self.tv_template = ""
        self.pallet_template = ""

    @classmethod
    def is_pallet_chosen(cls):
        return len(cls.current_chosen_palet) > 0

    @classmethod
    def get_pallet_chosen(cls):
        return cls.current_chosen_palet

    @classmethod
    def set_pallet_chosen(cls, text: str):
        cls.current_chosen_palet = text

    def get_tv_template(self):
        return self.tv_template

    def get_pallet_template(self):
        return self.pallet_template

    def set_tv_template(self, string: str):
        self.tv_template = string

    def set_pallet_template(self, string: str):
        self.pallet_template = string

    @staticmethod
    def is_pattern_match(pattern: str, data: str) -> bool:
        if len(pattern) == len(data):
            pattern.upper()
            data.upper()
            divided_patten = list(pattern)
            divided_data = list(data)
            for symbol in range(len(divided_patten)):
                if divided_patten[symbol] == '*':
                    pass
                else:
                    if divided_patten[symbol] == divided_data[symbol]:
                        pass
                    else:
                        return False
            return True
        else:
            return False
