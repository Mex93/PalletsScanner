import configparser
from os import path
from cryptography.fernet import Fernet

from sql.CSQLAgent import CSqlAgent
from enums import JOB_TYPE, REPEAT_TV_ERROR_TYPES
MAX_PALLET_PLACES = 60


class ConfigError(Exception):
    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class CConfig:
    def __init__(self):
        self.__SQL_USER_NAME = ''
        self.__SQL_PASSWORD = ''
        self.__SQL_HOST = ''
        self.__SQL_PORT = ''
        self.__SQL_DATABASE = ''
        self.__SOFT_TYPE = ''  # Тип работы программы [0 - внесение, 1 - просмотр из бд]
        self.__PALLET_ALL_PLACES = ''  # Сколько на паллете телеков
        self.__PALLET_AUTO_COMPLETE = ''  # Автоматически закрывать паллет, если количество уже == максимальному
        self.__PALLET_TEMPLATE = ''  # Шаблон номера паллета
        self.__TV_TEMPLATE = ''  # Шаблон телевизора
        self.__TV_REPEAT_ERROR_TYPE = ''  # Тип ошибки про повтор телека - 0 - Окно с подтверждением, 1 - Просто в чат
        self.__CURRENT_LINE = ''  # Текущая производственная линия
        self.__AUTO_COMPLETE_WINDOW = ''  # Окно автозавершения паллета

        self.__PRINTER_NAME = ''  # Название принтера
        self.__TRICOLOR_USED = ''  # Включить или отключить проверку телеков на триколор

        self.__config = configparser.ConfigParser()
        self.__config.add_section('database')
        self.__config.add_section('program')
        self.__config.add_section('pallet')
        self.__config.add_section('tv')

    def set_default_for_values(self):
        self.__SQL_USER_NAME = ''
        self.__SQL_PASSWORD = ''
        self.__SQL_HOST = ''
        self.__SQL_PORT = ''
        self.__SQL_DATABASE = ''
        self.__SOFT_TYPE = ''
        self.__PALLET_ALL_PLACES = ''
        self.__PALLET_AUTO_COMPLETE = ''
        self.__PALLET_TEMPLATE = ''
        self.__TV_TEMPLATE = ''
        self.__TV_REPEAT_ERROR_TYPE = ''
        self.__CURRENT_LINE = ''
        self.__AUTO_COMPLETE_WINDOW = ''
        self.__PRINTER_NAME = ''
        self.__TRICOLOR_USED = ''

    def get_config(self):
        self.__config.read('config.ini', encoding="utf-8")

        self.__SQL_USER_NAME = self.__config.get('database', 'SQL_USER_NAME')
        self.__SQL_PASSWORD = self.__config.get('database', 'SQL_PASSWORD')
        self.__SQL_HOST = self.__config.get('database', 'SQL_HOST')
        self.__SQL_PORT = self.__config.get('database', 'SQL_PORT')
        self.__SQL_DATABASE = self.__config.get('database', 'SQL_DATABASE')

        self.__SOFT_TYPE = self.__config.get('program', 'PROGRAM_JOB_TYPE')
        self.__CURRENT_LINE = self.__config.get('program', 'CURRENT_ASSEMBLED_LINE')
        self.__TRICOLOR_USED = self.__config.get('program', 'TRICOLOR_USED')
        self.__PRINTER_NAME = self.__config.get('program', 'PRINTER_NAME')

        self.__PALLET_ALL_PLACES = self.__config.get('pallet', 'PALLET_MAX_PLACES')
        self.__PALLET_AUTO_COMPLETE = self.__config.get('pallet', 'PALLET_AUTO_COMPLETE')
        self.__PALLET_TEMPLATE = self.__config.get('pallet', 'PALLET_TEMPLATE')
        self.__AUTO_COMPLETE_WINDOW = self.__config.get('pallet', 'PALLET_AUTO_COMPLETE_WINDOW')

        self.__TV_TEMPLATE = self.__config.get('tv', 'TV_TEMPLATE')
        self.__TV_REPEAT_ERROR_TYPE = self.__config.get('tv', 'TV_REPEAT_ERROR_TYPE')


    @staticmethod
    def is_config_created():
        if path.isfile('config.ini') is True:
            return True
        return False

    def create_config(self):
        with open('config.ini', 'w') as config_file:
            self.__config.set('database', 'SQL_USER_NAME', 'This place for user!')
            self.__config.set('database', 'SQL_PASSWORD', 'This place for user password!')
            self.__config.set('database', 'SQL_HOST', 'This place for db host!')
            self.__config.set('database', 'SQL_PORT', 'This place for db port!')
            self.__config.set('database', 'SQL_DATABASE', 'This place for db name!')

            self.__config.set('program', 'PROGRAM_JOB_TYPE', str(JOB_TYPE.MAIN))
            self.__config.set('program', 'CURRENT_ASSEMBLED_LINE', "1")
            self.__config.set('program', 'TRICOLOR_USED', "0")
            self.__config.set('program', 'PRINTER_NAME', "NO")

            self.__config.set('pallet', 'PALLET_MAX_PLACES', '2')
            self.__config.set('pallet', 'PALLET_AUTO_COMPLETE', '1')
            self.__config.set('pallet', 'PALLET_TEMPLATE', '****24****')
            self.__config.set('pallet', 'PALLET_AUTO_COMPLETE_WINDOW', '1')

            self.__config.set('tv', 'TV_TEMPLATE', '*******')
            self.__config.set('tv', 'TV_REPEAT_ERROR_TYPE', '0')

            self.set_default_for_values()
            self.__config.write(config_file)

    def get_printer_name(self) -> str | bool:
        len_prname = len(self.__PRINTER_NAME)
        if not len_prname:
            return "NO"
        if len_prname < 3:
            return "NO"
        return self.__PRINTER_NAME

    def is_tricolor_used(self) -> bool:
        len_prname = len(self.__TRICOLOR_USED)
        if not len_prname:
            return False
        len_prname = bool(self.__TRICOLOR_USED)
        if len_prname != 0 and len_prname != 1:
            return False
        return len_prname

    def get_current_line(self) -> int | None:
        line = int(self.__CURRENT_LINE)
        if 1 <= line <= 4:
            return line
        return None

    def get_repeat_tv_error_type(self) -> REPEAT_TV_ERROR_TYPES:
        error_type = int(self.__TV_REPEAT_ERROR_TYPE)
        if error_type == 0:
            return REPEAT_TV_ERROR_TYPES.WINDOW
        elif error_type == 1:
            return REPEAT_TV_ERROR_TYPES.CHAT_MESSAGE
        else:
            return REPEAT_TV_ERROR_TYPES.WINDOW


    def get_pallet_template(self) -> str:
        template = self.__PALLET_TEMPLATE
        lengt = len(template)
        if lengt >= 4:
            return template
        return "DDMMYYXXXX"

    def get_tv_template(self) -> str:
        template = self.__TV_TEMPLATE
        lengt = len(template)
        if lengt >= 4:
            return template
        return "**********"

    def get_pallet_max_places(self) -> int:
        numb = int(self.__PALLET_ALL_PLACES)
        print(numb)
        if 1 <= numb <= MAX_PALLET_PLACES:
            return numb
        return 2

    def get_pallet_auto_completed(self) -> bool:
        numb = int(self.__PALLET_AUTO_COMPLETE)
        if numb in (0, 1):
            return bool(numb)
        return False

    def get_pallet_autocomplete_window(self) -> bool:
        numb = int(self.__AUTO_COMPLETE_WINDOW)
        if numb in (0, 1):
            return bool(numb)
        return False

    def get_soft_job_type(self) -> int:
        """Тип работы программы [0 - внесение, 1 - просмотр из бд]"""
        numb = int(self.__SOFT_TYPE)
        if numb in (JOB_TYPE.MAIN, JOB_TYPE.INFO):
            return numb
        return JOB_TYPE.MAIN

    def get_dbpassword(self):
        return self.__SQL_PASSWORD

    def get_dbuser(self):
        return self.__SQL_USER_NAME

    def get_dbhost(self):
        return self.__SQL_HOST

    def get_dbport(self):
        return self.__SQL_PORT

    def get_dname(self):
        return self.__SQL_DATABASE

    def save_config(self):
        if self.is_config_created() is False:
            with open('config.ini', 'w') as config_file:
                self.__config.write(config_file)

    def load_data(self):
        if self.is_config_created():
            self.get_config()
        else:
            self.create_config()
            self.get_config()

        db_name = self.get_dname()
        db_user = self.get_dbuser()
        db_pass = self.get_dbpassword()
        db_port = self.get_dbport()
        db_host = self.get_dbhost()

        # crypto_key = Fernet.generate_key()
        # print("keu: " + str(crypto_key))
        crypto_key = "OWChcLRfYg7QtEkaLYw_g-594QPRFmrsEQxMWry0wVQ="  # ключ для расшифровки
        cipher_suite = Fernet(crypto_key)

        # db_standart_connect_params = {
        #     KEY_VALUE_NAME_USER: 'test_user',
        #     KEY_VALUE_NAME_PASS: 'sadmin',
        #     KEY_VALUE_NAME_DATABASE: 'test_db',
        #     KEY_VALUE_NAME_HOST: '192.168.7.182',
        #     KEY_VALUE_NAME_PORT: '5432'
        # }

        # cipher_text = cipher_suite.encrypt(b"program_palletscanner")
        # print(cipher_text)
        # cipher_text = cipher_suite.encrypt(b"UG5de7g6FGryxs67TGhuV")
        # print(cipher_text)
        # cipher_text = cipher_suite.encrypt(b"assemblyproduction")
        # print(cipher_text)

        set_config_error = False
        db_params = (db_name, db_user, db_pass, db_port, db_host)
        for value in db_params:
            if value is False or value is None or value.find("This") != -1:
                # this error
                set_config_error = True
                break

        if set_config_error is False:
            # decode
            try:
                db_name = cipher_suite.decrypt(db_name)
                db_name = db_name.decode()
                db_user = cipher_suite.decrypt(db_user)
                db_user = db_user.decode()
                db_pass = cipher_suite.decrypt(db_pass)
                db_pass = db_pass.decode()

            except:
                set_config_error = True

            if set_config_error is False:

                db_params = (db_name, db_user, db_pass)
                for value in db_params:
                    if value is False or value is None or value.find("This") != -1:
                        # this error
                        set_config_error = True
                        break

                if set_config_error is False:
                    sql_data: dict = {
                        CSqlAgent.get_value_name_database(): db_name,
                        CSqlAgent.get_value_name_user(): db_user,
                        CSqlAgent.get_value_name_host(): db_host,
                        CSqlAgent.get_value_name_port(): db_port,
                        CSqlAgent.get_value_name_pass(): db_pass,
                    }
                    # print(sql_data)
                    CSqlAgent.set_sql_data_line(sql_data)

        if set_config_error is True:
            return False

        return True
