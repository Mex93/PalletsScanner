from sql.CSQLAgent import CSqlAgent
from sql.sql_data import SQL_TABLE_NAME, SQL_TV_MODEL_INFO_FIELDS, SQL_ASSEMBLED_TV_FIELDS


class CSQLQuerys(CSqlAgent):
    MAX_LIMIT_TV_COUNTS = 100_000

    def __init__(self):
        super().__init__()

    def get_models_list(self):
        query_string = (f"SELECT "
                        f"{SQL_TV_MODEL_INFO_FIELDS.tvmi_fd_tv_id}, "
                        f"{SQL_TV_MODEL_INFO_FIELDS.tvmi_fd_tv_name} "
                        f"FROM {SQL_TABLE_NAME.tv_model_info_tv} "
                        f"ORDER BY {SQL_TV_MODEL_INFO_FIELDS.tvmi_fd_tv_id} ASC "
                        f"LIMIT 100")  # на всякий лимит

        result = self.sql_query_and_get_result(
            self.get_sql_handle(), query_string, (), "_1", )  # Запрос типа аасоциативного массива
        if result is False:  # Errorrrrrrrrrrrrr based data
            return False
        # print(result)

        sql_pass = result[0].get(SQL_TV_MODEL_INFO_FIELDS.tvmi_fd_tv_name, None)
        if sql_pass is not None:
            return True, result
        return False

    def get_data_list(self,
                      tv_fk: int,
                      assembled_line: int,
                      query_fields_list: list,
                      start_unix_date: str, end_unix_date: str):

        query_fields_str = ','.join(query_fields_list)
        if query_fields_str:

            query_string = (f"SELECT {query_fields_str} "
                            f"FROM {SQL_TABLE_NAME.assembled_tv} "
                            f"WHERE "
                            f"({SQL_ASSEMBLED_TV_FIELDS.fd_linefk} = {assembled_line} AND "
                            f"{SQL_ASSEMBLED_TV_FIELDS.fd_tvfk} = {tv_fk}) AND "
                            f"( {SQL_ASSEMBLED_TV_FIELDS.fd_completed_date} >= '{start_unix_date}' AND "
                            f"{SQL_ASSEMBLED_TV_FIELDS.fd_completed_date}  <= '{end_unix_date}' ) "
                            f"ORDER BY {SQL_ASSEMBLED_TV_FIELDS.fd_assy_id} ASC "
                            f"LIMIT {self.MAX_LIMIT_TV_COUNTS}")  # на всякий лимит

            result = self.sql_query_and_get_result(
                self.get_sql_handle(), query_string, (), "_1", )  # Запрос типа аасоциативного массива
            if result is False:  # Errorrrrrrrrrrrrr based data
                return False
            # print(result)

            sql_pass = result[0].get(SQL_ASSEMBLED_TV_FIELDS.fd_tv_sn, None)
            if sql_pass is not None:
                return True, result
        return False
