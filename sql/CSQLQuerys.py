from sql.CSQLAgent import CSqlAgent
from sql.sql_data import (SQL_TABLE_NAME,
                          SQL_PALLET_SCANNED,
                          SQL_PALLET_SN,
                          SQL_TABLE_TV_CONFIG,
                          SQL_TABLE_ASSEMBLED_TV)
from config_parser.CConfig import MAX_PALLET_PLACES


class CSQLQuerys(CSqlAgent):
    MAX_LIMIT_TV_COUNTS = 100_000

    def __init__(self):
        super().__init__()

    def is_created_pallet(self, pallet_code: str):
        """А создан ли вообще паллет"""
        query_string = (f"SELECT {SQL_PALLET_SN.fd_assy_id} "
                        f"FROM {SQL_TABLE_NAME.tb_pallet_sn} "
                        f"WHERE {SQL_PALLET_SN.fd_pallet_code} = %s "
                        f"ORDER BY {SQL_PALLET_SN.fd_assy_id} ASC "
                        f"LIMIT 1")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (pallet_code,), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        sql_pass = result[0].get(SQL_PALLET_SN.fd_assy_id, None)
        if sql_pass is not None:
            return True

        return False

    def delete_tv_sn_from_pallet_scanned(self, tv_sn: str, pallet_code: str):
        """Удалить телек на паллете из таблицы с паллетами"""
        query_string = (f"DELETE FROM {SQL_TABLE_NAME.tb_pallet_scanned} "
                        f"WHERE "
                        f"{SQL_PALLET_SCANNED.fd_tv_sn} = %s  AND {SQL_PALLET_SCANNED.fd_fk_pallet_code} = %s")

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (tv_sn, pallet_code,), "_d", )
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        return True

    def get_pallet_info(self, pallet_code: str):
        """Инфа о паллете"""
        query_string = (f"SELECT * "
                        f"FROM {SQL_TABLE_NAME.tb_pallet_scanned} "
                        f"WHERE {SQL_PALLET_SCANNED.fd_fk_pallet_code} = %s "
                        f"ORDER BY {SQL_PALLET_SCANNED.fd_assy_id} ASC "
                        f"LIMIT {MAX_PALLET_PLACES}")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (pallet_code,), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False
        # print(result)

        return result

    def is_pallet_have_any_sn(self, pallet_code: str):
        """Инфа о паллете"""
        query_string = (f"SELECT * "
                        f"FROM {SQL_TABLE_NAME.tb_pallet_scanned} "
                        f"WHERE {SQL_PALLET_SCANNED.fd_fk_pallet_code} = %s "
                        f"LIMIT 1")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (pallet_code,), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False
        # print(result)
        if len(result) > 0:
            return True

        return False

    def get_tv_info(self, tv_sn: str) -> bool | dict:
        """Инфа о телевизоре"""
        query_string = (f"SELECT "
                        f"{SQL_TABLE_NAME.tb_tv_models}.{SQL_TABLE_TV_CONFIG.fd_tv_name},"
                        f"{SQL_TABLE_NAME.tb_tv_models}.{SQL_TABLE_TV_CONFIG.fd_tv_id}, "
                        f"{SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_tv_sn}, "
                        f"{SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_sn_scan_time}, "
                        f"{SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_first_scan_time}, "
                        f"{SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_completed_scan_time} "
                        f"FROM {SQL_TABLE_NAME.tb_assembled_tv} "
                        f"JOIN {SQL_TABLE_NAME.tb_tv_models} "
                        f"ON "
                        f"{SQL_TABLE_NAME.tb_tv_models}.{SQL_TABLE_TV_CONFIG.fd_tv_id} = "
                        f"{SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_tv_fk} "
                        f"WHERE {SQL_TABLE_NAME.tb_assembled_tv}.{SQL_TABLE_ASSEMBLED_TV.fd_tv_sn} = %s "
                        f"LIMIT 1")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (tv_sn,), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        # print(result)

        return result[0]

    def insert_scanned_tv_on_pallet(self, pallet_code: str, tv_sn: str, tv_fk: int) -> int | bool:
        """Вставить тв в паллет """

        query_string = (f"INSERT INTO "
                        f"{SQL_TABLE_NAME.tb_pallet_scanned}"
                        f"("
                        f"{SQL_PALLET_SCANNED.fd_fk_pallet_code}, "
                        f"{SQL_PALLET_SCANNED.fd_tv_sn}, "
                        f"{SQL_PALLET_SCANNED.fd_tv_model_fk}"
                        f") VALUES"
                        f"(%s, %s, %s) "
                        f"RETURNING {SQL_PALLET_SCANNED.fd_assy_id}")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (pallet_code, tv_sn, tv_fk), "_i", )
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        sql_pass = result[0][0]  # возвращает кортеж с одним элементом
        if sql_pass is None:
            return False

        return sql_pass

    def set_completed_status(self, pallet_code: str, check_variant: bool) -> int | bool:
        """ Проставить чек комплектности
        False - не закрыт и установка даты текущей,
        True - проставляет комплектность и дата текущей """
        if isinstance(check_variant, bool):

            query_string = (f"UPDATE {SQL_TABLE_NAME.tb_pallet_sn} SET "
                            f"{SQL_PALLET_SN.fd_completed_check} = {check_variant},"
                            f"{SQL_PALLET_SN.fd_completed_time} = now() "
                            f"WHERE {SQL_PALLET_SN.fd_pallet_code} = %s "
                            )

            result = self.sql_query_and_get_result(
                self.get_sql_handle(), query_string, (pallet_code,), "_u", )
            return result
        return False

    def create_new_pallet(self, pallet_code: str) -> int | bool:
        """ Создать паллет """

        query_string = (f"INSERT INTO "
                        f"{SQL_TABLE_NAME.tb_pallet_sn}"
                        f"("
                        f"{SQL_PALLET_SN.fd_pallet_code}"
                        f") VALUES"
                        f"(%s) "
                        f"RETURNING {SQL_PALLET_SN.fd_assy_id}")

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (pallet_code, ), "_i", )
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        sql_pass = result[0][0]  # возвращает кортеж с одним элементом
        if sql_pass is None:
            return False

        return sql_pass

    def get_pallet_id_from_tv_sn(self, tv_sn: str) -> str | bool:
        """Проверка на наличие tv sn в других паллетах """
        query_string = (f"SELECT "
                        f"{SQL_PALLET_SCANNED.fd_assy_id}, "
                        f"{SQL_PALLET_SCANNED.fd_fk_pallet_code}, "
                        f"{SQL_PALLET_SCANNED.fd_tv_model_fk} "
                        f"FROM {SQL_TABLE_NAME.tb_pallet_scanned} "
                        f"WHERE {SQL_PALLET_SCANNED.fd_tv_sn} = %s "
                        f"ORDER BY {SQL_PALLET_SCANNED.fd_assy_id} ASC "
                        f"LIMIT 1")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (tv_sn,), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False

        sql_pass = result[0].get(SQL_PALLET_SCANNED.fd_fk_pallet_code, None)
        if sql_pass is None:
            return False

        return sql_pass

        # print(result)

