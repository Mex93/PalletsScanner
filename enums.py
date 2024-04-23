from enum import IntEnum, auto


class CHECK_BOX_TYPE(IntEnum):
    DB_ID = auto(),
    TV_FK = auto(),
    TV_NAME = auto(),
    LINE_FK = auto(),
    TV_SN = auto(),
    WIFI_MODULE_SN = auto(),
    BT_MODULE_SN = auto(),
    MAC = auto(),
    PANEL_SN = auto(),
    OC_SN = auto(),
    MB_SN = auto(),
    PB_SN = auto(),
    TCON_SN = auto(),
    OPS_SN = auto(),
    SCAN_DATE = auto(),
    SN_SCAN_DATE = auto(),
    PACK_SCAN_DATE = auto(),


class BUTTOM_TYPE(IntEnum):
    LOAD = 0,
    SAVE = 1
    RESET = 2,


class DATE_BOX_TYPE(IntEnum):
    START = auto(),
    END = auto()


class SMBOX_ICON_TYPE(IntEnum):
    ICON_NONE = auto(),
    ICON_WARNING = auto(),
    ICON_ERROR = auto(),
    ICON_INFO = auto(),
    ICON_SUCCESS = auto()


class LINE_ID(IntEnum):
    FIRST = auto(),
    TWO = auto(),
    THREE = auto(),
    FOUR = auto(),
    KZ = auto()


class LIST_MODELS(IntEnum):
    MODEL_FK = 0,
    MODEL_NAME = 1,
    MODEL_VAR = 2,
    MODEL_TYPE = 3,


class LIST_MODELS_NO_VAR(IntEnum):
    MODEL_FK = 0,
    MODEL_NAME = 1,
    MODEL_TYPE = 2,


class CB_ARR_TYPE(IntEnum):
    TYPE = 0,
    WINDOW_VAR = 1,
    STANDART_STATUS = 1,
    SQL_FIELD = 2,
    RESULT_TYPE = 3,


class RESULT_DATA(IntEnum):
    DB_ID = auto(),
    TV_FK = auto(),
    TV_NAME = auto(),
    LINE_FK = auto(),
    TV_SN = auto(),
    WIFI_MODULE_SN = auto(),
    BT_MODULE_SN = auto(),
    MAC = auto(),
    PANEL_SN = auto(),
    OC_SN = auto(),
    MB_SN = auto(),
    PB_SN = auto(),
    TCON_SN = auto(),
    OPS_SN = auto(),
    SCAN_DATE = auto(),
    SN_SCAN_DATE = auto(),
    PACK_SCAN_DATE = auto(),


class RESULT_FIELDS_TYPES(IntEnum):
    TYPE = 0,
    DICT_NAME = 1,
    HUMAN_NAME = 2


class TIME_ZONE(IntEnum):
    NONE = 0,
    RF = 1,
    KZ = 2,


class TIME_ZONES_ARR_TYPE(IntEnum):
    TEXT = 0,
    ZONE_ID = 1,
    VAR = 2


class MENU_INFO_TYPE(IntEnum):
    HOW_TO_USE = auto(),
    RULES = auto(),
    ABOUT = auto(),
