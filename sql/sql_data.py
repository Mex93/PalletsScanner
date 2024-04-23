# Название всех таблиц скрипта
class SQL_TABLE_NAME:
    assembled_tv = "assembled_tv"
    tv_model_info_tv = "tv"


# Название полей в конфиге готовых тв
class SQL_ASSEMBLED_TV_FIELDS:
    fd_assy_id = "assy_id"
    fd_tvfk = "tv_fk"
    fd_linefk = "line_fk"  # Линия вторичный ключ
    fd_tv_sn = "tv_sn"
    fd_tv_mac = "ethernet_mac"
    fd_tv_mb_sn = "mainboard_sn"
    fd_tv_wifi_mac = "wifi_module_sn"
    fd_tv_bt_mac = "bt_module_sn"
    fd_tv_panel_sn = "lcm_sn"
    fd_tv_oc_sn = "oc_sn"
    fd_tv_pb_sn = "powerboard_sn"
    fd_tv_tcon_sn = "tcon_sn"
    fd_tv_ops_sn = "ops_sn"
    fd_tv_sn_date = "timestamp_st60"  # присвоение SN
    fd_tv_scan_date = "timestamp_st10"  # Сканировка первичная

    fd_completed_date = "timestamp_st100"  # Дата прохождения черезе упаковку

class SQL_TV_MODEL_INFO_FIELDS:
    tvmi_fd_tv_id = "tv_id"
    tvmi_fd_tv_name = "tv_name"
    tvmi_fd_vendor_code = "vendor_code"
    tvmi_fd_tv_platform_fk = "tv_platform_fk"
    tvmi_fd_scan_type_fk = "scan_type_fk"
    tvmi_fd_software_type_fk = "software_type_fk"
    tvmi_fd_tv_serial_number_template = "tv_serial_number_template"

