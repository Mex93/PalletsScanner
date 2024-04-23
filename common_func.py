from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize
from enums import SMBOX_ICON_TYPE

INFO_CURRENT_ADMIN_EMAIL = "ryazanov.n@tvkvant.ru"


def get_rules_text() -> str:
    return (
        "Приведённые правила использования программы обязательны к соблюдению всем пользователям.\n\n"
        "Перечень:\n"
        "1) Разглашение данных предоставляемых программой сторонним лицам, не имеющим отношения к 'ООО Квант', "
        "строго запрещено!\n"
        "2) Попытка декомпиляции и любое вредительство внутри рабочей директории программы строго "
        "запрещено и снимает с разработчика ответственность за возможный ущерб.\n"
        "3) Перед использованием программы пользователь должен быть ознакомлен с инструкцией.\n"
        "4) Для корректной работы программы пользователь должен указывать корректные данные в формы для заполнения.\n"
        "5) Разработчик имеет право вносить любые изменения в программу и документацию без уведомления пользователей.\n"
        "6) Невыполнение любого из пунктов правил влечёт нарушение пользователем своих обязательств."
    )


def get_about_text() -> str:
    current_year = datetime.now().year
    return ("Программа для формирования паллетов готовой продукции TCL.\n\n"
            "Все права принадлежат ООО 'Квант'.\n\n"
            "Разработчик: Рязанов Н.В.\n"
            f"По всем интересующим вопросам и пожеланиям обращайтесь на почту {INFO_CURRENT_ADMIN_EMAIL}\n\n"
            f"\t\t\t{current_year} г.")


def get_instruction_text() -> str:
    return (
        "Программа предназначена для выгрузки данных любого типа устройства, собранного на сборочном конвейере и "
        "прошедшего процесс сканировки компонентов.\n\n"
        "- Для корректной выгрузки данных вам нужно указать:\n"
        "1) Правильный временной интервал выгрузки. Дата начала и дата конца сборки желаемого типа устройства.\n"
        "Выберите нужную дату в календаре и введите желаемый час в формате 24 часа.\n"
        "2) Выберите из списка модель устройства или введите вручную, в специальную форму.\n"
        "3) Если результат выборки отсутствует, то вы могли просто ошибиться в указанни данных для фильтра.\n\n"
        "- Последовательность операций для выгрузки данных:\n"
        "1) Заполните данные для фильтра выборки в соответствующие формы программы.\n"
        "2) Нажмите на кнопку 'Выбрать данные', после чего, при удачной выборке, вы будете оповещены в окне меню "
        "результата.\n"
        "3) Если результат выборки есть, вы можете нажать на кнопку 'Сохранить в EXCEL', программа предложит выбрать "
        "путь для сохранения файла.\n"
        "4) С помощью меню, сохраните файл с результатом в любое месте своего устройства.\n"
        "5) Для запроса другого результата вам потребуется очистить старый результат, нажав на кнопку 'Очистить' "
        ", после чего вы сможете указать новые данные для фильтра и выполнить запрос.\n\n"
    )


def send_message_box(icon_style, text: str, title: str, variant_yes: str, variant_no: str, callback=None):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    match icon_style:
        case _, SMBOX_ICON_TYPE.ICON_NONE:
            msg.setIcon(QMessageBox.Icon.NoIcon)
        case SMBOX_ICON_TYPE.ICON_ERROR:
            msg.setIcon(QMessageBox.Icon.Critical)
        case SMBOX_ICON_TYPE.ICON_WARNING:
            msg.setIcon(QMessageBox.Icon.Warning)
        case SMBOX_ICON_TYPE.ICON_INFO:
            msg.setIcon(QMessageBox.Icon.Information)
        case SMBOX_ICON_TYPE.ICON_SUCCESS:
            pass

    icon = QIcon()
    icon.addFile(u":/img/logo.ico", QSize(), QIcon.Normal, QIcon.Off)

    msg.setWindowIcon(icon)
    if len(variant_yes) > 0:
        msg.addButton(variant_yes, QtWidgets.QMessageBox.ButtonRole.YesRole)
    if len(variant_no) > 0:
        msg.addButton(variant_no, QtWidgets.QMessageBox.ButtonRole.NoRole)
    msg.setText(text)

    font = QFont()
    font.setFamilies([u"Segoe UI Emoji"])
    font.setPointSize(12)
    msg.setFont(font)

    if callback is not None:
        msg.buttonClicked.connect(callback)

    msg.exec()
    return msg


def get_current_unix_time() -> int:
    return int(int(datetime.now().timestamp()))


def convert_date_from_sql_format(date: str):
    string = date.split(".")[0]
    if string is False:
        string = ""
    return string
