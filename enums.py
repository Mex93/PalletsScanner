from enum import IntEnum, auto


class JOB_TYPE(IntEnum):
    MAIN = 0,
    INFO = 1


class REPEAT_TV_ERROR_TYPES(IntEnum):
    WINDOW = 0,
    CHAT_MESSAGE = 1


class SMBOX_ICON_TYPE(IntEnum):
    ICON_NONE = auto(),
    ICON_WARNING = auto(),
    ICON_ERROR = auto(),
    ICON_INFO = auto()


class BARCODE_TYPE(IntEnum):
    BAR_4 = auto(),
    BAR_8 = auto(),
    BAR_12 = auto(),
    BAR_16 = auto(),
    BAR_24 = auto(),
    BAR_32 = auto(),
    BAR_48 = auto()
