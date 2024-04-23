# Пропикивание паллетов для телевизоров TCL

import sys
from Window import MainWindow

from PySide6.QtWidgets import QApplication
# pyside6-uic .\ui\untitled.ui -o .\ui\untitled.py
# pyside6-rcc .\ui\res.qrc -o .\ui\res_rc.py
#  pip freeze > requirements.txt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
