# Название всех таблиц скрипта
class SQL_TABLE_NAME:
    tb_pallet_scanned = "pallets_scanned"
    tb_pallet_sn = "pallets_sn"
    tb_tv_models = "tv"
    tb_assembled_tv = "assembled_tv"


# Название полей в конфиге готовых тв
class SQL_PALLET_SN:  # таблица созданных паллетов
    fd_assy_id = "assy_id"
    fd_pallet_code = "pallet_code"  # номер паллет
    fd_created_data = "created_data"  # Дата создания
    fd_completed_check = "completed_check"  # Чек готовности
    fd_completed_time = "completed_date"  # Чек даты готовности

class SQL_PALLET_SCANNED:  # таблица привязки телеков к палеткам
    fd_assy_id = "assy_id"
    fd_fk_pallet_code = "pallet_code"  # номер паллет
    fd_created_data = "created_data"  # Дата создания
    fd_tv_sn = "tv_sn"  # серийник телека
    fd_tv_model_fk = "tv_model_fk"  # номер модели


class SQL_TABLE_ASSEMBLED_TV:  # Таблица собранных телевизоров
    fd_assy_id = "assy_id"
    fd_tv_fk = "tv_fk"
    fd_tv_sn = "tv_sn"  # Линия вторичный ключ

    fd_first_scan_time = "timestamp_st10"  # Время сканировки первичной
    fd_completed_scan_time = "timestamp_st100"  # Дата прохождения черезе упаковку
    fd_sn_scan_time = "timestamp_st60"  # Дата прохождения черезе присвоение sn


class SQL_TABLE_TV_CONFIG:  # Таблица с моделями
    fd_tv_id = "tv_id"
    fd_tv_name = "tv_name"
