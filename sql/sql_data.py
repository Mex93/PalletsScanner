# Название всех таблиц скрипта
class SQL_TABLE_NAME:
    tb_pallet_scanned = "pallets_scanned"
    tb_pallet_sn = "pallets_sn"


# Название полей в конфиге готовых тв
class SQL_PALLET_SN:  # таблица созданных паллетов
    fd_assy_id = "assy_id"
    fd_pallet_code = "pallet_code"  # номер паллет
    fd_created_data = "created_data"  # Дата создания

class SQL_PALLET_SCANNED:  # таблица привязки телеков к палеткам
    fd_assy_id = "assy_id"
    fd_fk_pallet_code = "pallet_code"  # номер паллет
    fd_created_data = "created_data"  # Дата создания
    fd_tv_sn = "tv_sn"  # серийник телека


