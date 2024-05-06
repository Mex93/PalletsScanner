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
