# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1471, 802)
        MainWindow.setMinimumSize(QSize(1471, 802))
        icon = QIcon()
        icon.addFile(u":/images/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1471, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_Flashing = QGroupBox(self.centralwidget)
        self.groupBox_Flashing.setObjectName(u"groupBox_Flashing")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Flashing.sizePolicy().hasHeightForWidth())
        self.groupBox_Flashing.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.groupBox_Flashing.setFont(font)
        self.groupBox_Flashing.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_Flashing)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox_Flashing)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/pallet_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_pallet_name = QLabel(self.groupBox_Flashing)
        self.label_pallet_name.setObjectName(u"label_pallet_name")
        font1 = QFont()
        font1.setPointSize(25)
        self.label_pallet_name.setFont(font1)
#if QT_CONFIG(tooltip)
        self.label_pallet_name.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_pallet_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_pallet_name.setStyleSheet(u"background-color:none")
        self.label_pallet_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_pallet_name.setLineWidth(8)
        self.label_pallet_name.setTextFormat(Qt.TextFormat.AutoText)
        self.label_pallet_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_pallet_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.places_frame = QVBoxLayout()
        self.places_frame.setObjectName(u"places_frame")
        self.label_all_places = QLabel(self.groupBox_Flashing)
        self.label_all_places.setObjectName(u"label_all_places")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setUnderline(True)
        self.label_all_places.setFont(font2)

        self.places_frame.addWidget(self.label_all_places)

        self.label_last_places = QLabel(self.groupBox_Flashing)
        self.label_last_places.setObjectName(u"label_last_places")
        self.label_last_places.setFont(font2)

        self.places_frame.addWidget(self.label_last_places)


        self.horizontalLayout_4.addLayout(self.places_frame)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_frame = QVBoxLayout()
        self.btn_frame.setObjectName(u"btn_frame")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btn_frame.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_set_cancel = QPushButton(self.groupBox_Flashing)
        self.pushButton_set_cancel.setObjectName(u"pushButton_set_cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_set_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_set_cancel.setSizePolicy(sizePolicy1)
        self.pushButton_set_cancel.setMinimumSize(QSize(139, 29))
        self.pushButton_set_cancel.setMaximumSize(QSize(200, 40))
        self.pushButton_set_cancel.setBaseSize(QSize(139, 29))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_set_cancel.setFont(font3)
        self.pushButton_set_cancel.setStyleSheet(u"color: red")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete_forever_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_cancel.setIcon(icon1)
        self.pushButton_set_cancel.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButton_set_cancel)

        self.pushButton_set_complete = QPushButton(self.groupBox_Flashing)
        self.pushButton_set_complete.setObjectName(u"pushButton_set_complete")
        sizePolicy1.setHeightForWidth(self.pushButton_set_complete.sizePolicy().hasHeightForWidth())
        self.pushButton_set_complete.setSizePolicy(sizePolicy1)
        self.pushButton_set_complete.setMinimumSize(QSize(139, 29))
        self.pushButton_set_complete.setMaximumSize(QSize(200, 40))
        self.pushButton_set_complete.setSizeIncrement(QSize(139, 29))
        self.pushButton_set_complete.setBaseSize(QSize(139, 29))
        self.pushButton_set_complete.setFont(font3)
        self.pushButton_set_complete.setStyleSheet(u"color: green\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/task_alt_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_set_complete.setIcon(icon2)
        self.pushButton_set_complete.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButton_set_complete)


        self.btn_frame.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.btn_frame)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_Flashing)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_leinfo = QLabel(self.groupBox_3)
        self.label_leinfo.setObjectName(u"label_leinfo")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_leinfo.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_leinfo)

        self.le_main = QLineEdit(self.groupBox_3)
        self.le_main.setObjectName(u"le_main")
        sizePolicy.setHeightForWidth(self.le_main.sizePolicy().hasHeightForWidth())
        self.le_main.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.le_main.setFont(font5)
        self.le_main.setInputMask(u"")
        self.le_main.setText(u"")
        self.le_main.setMaxLength(40)
        self.le_main.setFrame(True)
        self.le_main.setEchoMode(QLineEdit.EchoMode.Normal)
        self.le_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_main.setDragEnabled(False)
        self.le_main.setPlaceholderText(u"")
        self.le_main.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_main)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.gridLayout_inpallets_table = QGroupBox(self.centralwidget)
        self.gridLayout_inpallets_table.setObjectName(u"gridLayout_inpallets_table")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setUnderline(False)
        self.gridLayout_inpallets_table.setFont(font6)
        self.verticalLayout_2 = QVBoxLayout(self.gridLayout_inpallets_table)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_field_0 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_0.setObjectName(u"pushButton_field_0")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setUnderline(False)
        self.pushButton_field_0.setFont(font7)
        self.pushButton_field_0.setCheckable(False)
        self.pushButton_field_0.setAutoDefault(False)
        self.pushButton_field_0.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_0, 0, 0, 1, 1)

        self.pushButton_field_12 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_12.setObjectName(u"pushButton_field_12")
        self.pushButton_field_12.setFont(font7)
        self.pushButton_field_12.setCheckable(False)
        self.pushButton_field_12.setAutoDefault(False)
        self.pushButton_field_12.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_12, 0, 1, 1, 1)

        self.pushButton_field_24 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_24.setObjectName(u"pushButton_field_24")
        self.pushButton_field_24.setFont(font7)
        self.pushButton_field_24.setCheckable(False)
        self.pushButton_field_24.setAutoDefault(False)
        self.pushButton_field_24.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_24, 0, 2, 1, 1)

        self.pushButton_field_36 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_36.setObjectName(u"pushButton_field_36")
        self.pushButton_field_36.setFont(font7)
        self.pushButton_field_36.setCheckable(False)
        self.pushButton_field_36.setAutoDefault(False)
        self.pushButton_field_36.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_36, 0, 3, 1, 1)

        self.pushButton_field_48 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_48.setObjectName(u"pushButton_field_48")
        self.pushButton_field_48.setFont(font7)
        self.pushButton_field_48.setCheckable(False)
        self.pushButton_field_48.setAutoDefault(False)
        self.pushButton_field_48.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_48, 0, 4, 1, 1)

        self.pushButton_field_1 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_1.setObjectName(u"pushButton_field_1")
        self.pushButton_field_1.setFont(font7)
        self.pushButton_field_1.setCheckable(False)
        self.pushButton_field_1.setAutoDefault(False)
        self.pushButton_field_1.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_1, 1, 0, 1, 1)

        self.pushButton_field_13 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_13.setObjectName(u"pushButton_field_13")
        self.pushButton_field_13.setFont(font7)
        self.pushButton_field_13.setCheckable(False)
        self.pushButton_field_13.setAutoDefault(False)
        self.pushButton_field_13.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_13, 1, 1, 1, 1)

        self.pushButton_field_25 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_25.setObjectName(u"pushButton_field_25")
        self.pushButton_field_25.setFont(font7)
        self.pushButton_field_25.setCheckable(False)
        self.pushButton_field_25.setAutoDefault(False)
        self.pushButton_field_25.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_25, 1, 2, 1, 1)

        self.pushButton_field_37 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_37.setObjectName(u"pushButton_field_37")
        self.pushButton_field_37.setFont(font7)
        self.pushButton_field_37.setCheckable(False)
        self.pushButton_field_37.setAutoDefault(False)
        self.pushButton_field_37.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_37, 1, 3, 1, 1)

        self.pushButton_field_49 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_49.setObjectName(u"pushButton_field_49")
        self.pushButton_field_49.setFont(font7)
        self.pushButton_field_49.setCheckable(False)
        self.pushButton_field_49.setAutoDefault(False)
        self.pushButton_field_49.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_49, 1, 4, 1, 1)

        self.pushButton_field_2 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_2.setObjectName(u"pushButton_field_2")
        self.pushButton_field_2.setFont(font7)
        self.pushButton_field_2.setCheckable(False)
        self.pushButton_field_2.setAutoDefault(False)
        self.pushButton_field_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_2, 2, 0, 1, 1)

        self.pushButton_field_14 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_14.setObjectName(u"pushButton_field_14")
        self.pushButton_field_14.setFont(font7)
        self.pushButton_field_14.setCheckable(False)
        self.pushButton_field_14.setAutoDefault(False)
        self.pushButton_field_14.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_14, 2, 1, 1, 1)

        self.pushButton_field_26 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_26.setObjectName(u"pushButton_field_26")
        self.pushButton_field_26.setFont(font7)
        self.pushButton_field_26.setCheckable(False)
        self.pushButton_field_26.setAutoDefault(False)
        self.pushButton_field_26.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_26, 2, 2, 1, 1)

        self.pushButton_field_38 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_38.setObjectName(u"pushButton_field_38")
        self.pushButton_field_38.setFont(font7)
        self.pushButton_field_38.setCheckable(False)
        self.pushButton_field_38.setAutoDefault(False)
        self.pushButton_field_38.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_38, 2, 3, 1, 1)

        self.pushButton_field_50 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_50.setObjectName(u"pushButton_field_50")
        self.pushButton_field_50.setFont(font7)
        self.pushButton_field_50.setCheckable(False)
        self.pushButton_field_50.setAutoDefault(False)
        self.pushButton_field_50.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_50, 2, 4, 1, 1)

        self.pushButton_field_3 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_3.setObjectName(u"pushButton_field_3")
        self.pushButton_field_3.setFont(font7)
        self.pushButton_field_3.setCheckable(False)
        self.pushButton_field_3.setAutoDefault(False)
        self.pushButton_field_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_3, 3, 0, 1, 1)

        self.pushButton_field_15 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_15.setObjectName(u"pushButton_field_15")
        self.pushButton_field_15.setFont(font7)
        self.pushButton_field_15.setCheckable(False)
        self.pushButton_field_15.setAutoDefault(False)
        self.pushButton_field_15.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_15, 3, 1, 1, 1)

        self.pushButton_field_27 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_27.setObjectName(u"pushButton_field_27")
        self.pushButton_field_27.setFont(font7)
        self.pushButton_field_27.setCheckable(False)
        self.pushButton_field_27.setAutoDefault(False)
        self.pushButton_field_27.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_27, 3, 2, 1, 1)

        self.pushButton_field_39 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_39.setObjectName(u"pushButton_field_39")
        self.pushButton_field_39.setFont(font7)
        self.pushButton_field_39.setCheckable(False)
        self.pushButton_field_39.setAutoDefault(False)
        self.pushButton_field_39.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_39, 3, 3, 1, 1)

        self.pushButton_field_51 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_51.setObjectName(u"pushButton_field_51")
        self.pushButton_field_51.setFont(font7)
        self.pushButton_field_51.setCheckable(False)
        self.pushButton_field_51.setAutoDefault(False)
        self.pushButton_field_51.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_51, 3, 4, 1, 1)

        self.pushButton_field_4 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_4.setObjectName(u"pushButton_field_4")
        self.pushButton_field_4.setFont(font7)
        self.pushButton_field_4.setCheckable(False)
        self.pushButton_field_4.setAutoDefault(False)
        self.pushButton_field_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_4, 4, 0, 1, 1)

        self.pushButton_field_16 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_16.setObjectName(u"pushButton_field_16")
        self.pushButton_field_16.setFont(font7)
        self.pushButton_field_16.setCheckable(False)
        self.pushButton_field_16.setAutoDefault(False)
        self.pushButton_field_16.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_16, 4, 1, 1, 1)

        self.pushButton_field_28 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_28.setObjectName(u"pushButton_field_28")
        self.pushButton_field_28.setFont(font7)
        self.pushButton_field_28.setCheckable(False)
        self.pushButton_field_28.setAutoDefault(False)
        self.pushButton_field_28.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_28, 4, 2, 1, 1)

        self.pushButton_field_40 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_40.setObjectName(u"pushButton_field_40")
        self.pushButton_field_40.setFont(font7)
        self.pushButton_field_40.setCheckable(False)
        self.pushButton_field_40.setAutoDefault(False)
        self.pushButton_field_40.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_40, 4, 3, 1, 1)

        self.pushButton_field_52 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_52.setObjectName(u"pushButton_field_52")
        self.pushButton_field_52.setFont(font7)
        self.pushButton_field_52.setCheckable(False)
        self.pushButton_field_52.setAutoDefault(False)
        self.pushButton_field_52.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_52, 4, 4, 1, 1)

        self.pushButton_field_5 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_5.setObjectName(u"pushButton_field_5")
        self.pushButton_field_5.setFont(font7)
        self.pushButton_field_5.setCheckable(False)
        self.pushButton_field_5.setAutoDefault(False)
        self.pushButton_field_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_5, 5, 0, 1, 1)

        self.pushButton_field_17 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_17.setObjectName(u"pushButton_field_17")
        self.pushButton_field_17.setFont(font7)
        self.pushButton_field_17.setCheckable(False)
        self.pushButton_field_17.setAutoDefault(False)
        self.pushButton_field_17.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_17, 5, 1, 1, 1)

        self.pushButton_field_29 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_29.setObjectName(u"pushButton_field_29")
        self.pushButton_field_29.setFont(font7)
        self.pushButton_field_29.setCheckable(False)
        self.pushButton_field_29.setAutoDefault(False)
        self.pushButton_field_29.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_29, 5, 2, 1, 1)

        self.pushButton_field_41 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_41.setObjectName(u"pushButton_field_41")
        self.pushButton_field_41.setFont(font7)
        self.pushButton_field_41.setCheckable(False)
        self.pushButton_field_41.setAutoDefault(False)
        self.pushButton_field_41.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_41, 5, 3, 1, 1)

        self.pushButton_field_53 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_53.setObjectName(u"pushButton_field_53")
        self.pushButton_field_53.setFont(font7)
        self.pushButton_field_53.setCheckable(False)
        self.pushButton_field_53.setAutoDefault(False)
        self.pushButton_field_53.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_53, 5, 4, 1, 1)

        self.pushButton_field_6 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_6.setObjectName(u"pushButton_field_6")
        self.pushButton_field_6.setFont(font7)
        self.pushButton_field_6.setCheckable(False)
        self.pushButton_field_6.setAutoDefault(False)
        self.pushButton_field_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_6, 6, 0, 1, 1)

        self.pushButton_field_18 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_18.setObjectName(u"pushButton_field_18")
        self.pushButton_field_18.setFont(font7)
        self.pushButton_field_18.setCheckable(False)
        self.pushButton_field_18.setAutoDefault(False)
        self.pushButton_field_18.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_18, 6, 1, 1, 1)

        self.pushButton_field_30 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_30.setObjectName(u"pushButton_field_30")
        self.pushButton_field_30.setFont(font7)
        self.pushButton_field_30.setCheckable(False)
        self.pushButton_field_30.setAutoDefault(False)
        self.pushButton_field_30.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_30, 6, 2, 1, 1)

        self.pushButton_field_42 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_42.setObjectName(u"pushButton_field_42")
        self.pushButton_field_42.setFont(font7)
        self.pushButton_field_42.setCheckable(False)
        self.pushButton_field_42.setAutoDefault(False)
        self.pushButton_field_42.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_42, 6, 3, 1, 1)

        self.pushButton_field_54 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_54.setObjectName(u"pushButton_field_54")
        self.pushButton_field_54.setFont(font7)
        self.pushButton_field_54.setCheckable(False)
        self.pushButton_field_54.setAutoDefault(False)
        self.pushButton_field_54.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_54, 6, 4, 1, 1)

        self.pushButton_field_7 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_7.setObjectName(u"pushButton_field_7")
        self.pushButton_field_7.setFont(font7)
        self.pushButton_field_7.setCheckable(False)
        self.pushButton_field_7.setAutoDefault(False)
        self.pushButton_field_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_7, 7, 0, 1, 1)

        self.pushButton_field_19 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_19.setObjectName(u"pushButton_field_19")
        self.pushButton_field_19.setFont(font7)
        self.pushButton_field_19.setCheckable(False)
        self.pushButton_field_19.setAutoDefault(False)
        self.pushButton_field_19.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_19, 7, 1, 1, 1)

        self.pushButton_field_31 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_31.setObjectName(u"pushButton_field_31")
        self.pushButton_field_31.setFont(font7)
        self.pushButton_field_31.setCheckable(False)
        self.pushButton_field_31.setAutoDefault(False)
        self.pushButton_field_31.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_31, 7, 2, 1, 1)

        self.pushButton_field_43 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_43.setObjectName(u"pushButton_field_43")
        self.pushButton_field_43.setFont(font7)
        self.pushButton_field_43.setCheckable(False)
        self.pushButton_field_43.setAutoDefault(False)
        self.pushButton_field_43.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_43, 7, 3, 1, 1)

        self.pushButton_field_55 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_55.setObjectName(u"pushButton_field_55")
        self.pushButton_field_55.setFont(font7)
        self.pushButton_field_55.setCheckable(False)
        self.pushButton_field_55.setAutoDefault(False)
        self.pushButton_field_55.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_55, 7, 4, 1, 1)

        self.pushButton_field_8 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_8.setObjectName(u"pushButton_field_8")
        self.pushButton_field_8.setFont(font7)
        self.pushButton_field_8.setCheckable(False)
        self.pushButton_field_8.setAutoDefault(False)
        self.pushButton_field_8.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_8, 8, 0, 1, 1)

        self.pushButton_field_20 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_20.setObjectName(u"pushButton_field_20")
        self.pushButton_field_20.setFont(font7)
        self.pushButton_field_20.setCheckable(False)
        self.pushButton_field_20.setAutoDefault(False)
        self.pushButton_field_20.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_20, 8, 1, 1, 1)

        self.pushButton_field_32 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_32.setObjectName(u"pushButton_field_32")
        self.pushButton_field_32.setFont(font7)
        self.pushButton_field_32.setCheckable(False)
        self.pushButton_field_32.setAutoDefault(False)
        self.pushButton_field_32.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_32, 8, 2, 1, 1)

        self.pushButton_field_44 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_44.setObjectName(u"pushButton_field_44")
        self.pushButton_field_44.setFont(font7)
        self.pushButton_field_44.setCheckable(False)
        self.pushButton_field_44.setAutoDefault(False)
        self.pushButton_field_44.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_44, 8, 3, 1, 1)

        self.pushButton_field_56 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_56.setObjectName(u"pushButton_field_56")
        self.pushButton_field_56.setFont(font7)
        self.pushButton_field_56.setCheckable(False)
        self.pushButton_field_56.setAutoDefault(False)
        self.pushButton_field_56.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_56, 8, 4, 1, 1)

        self.pushButton_field_9 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_9.setObjectName(u"pushButton_field_9")
        self.pushButton_field_9.setFont(font7)
        self.pushButton_field_9.setCheckable(False)
        self.pushButton_field_9.setAutoDefault(False)
        self.pushButton_field_9.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_9, 9, 0, 1, 1)

        self.pushButton_field_21 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_21.setObjectName(u"pushButton_field_21")
        self.pushButton_field_21.setFont(font7)
        self.pushButton_field_21.setCheckable(False)
        self.pushButton_field_21.setAutoDefault(False)
        self.pushButton_field_21.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_21, 9, 1, 1, 1)

        self.pushButton_field_33 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_33.setObjectName(u"pushButton_field_33")
        self.pushButton_field_33.setFont(font7)
        self.pushButton_field_33.setCheckable(False)
        self.pushButton_field_33.setAutoDefault(False)
        self.pushButton_field_33.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_33, 9, 2, 1, 1)

        self.pushButton_field_45 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_45.setObjectName(u"pushButton_field_45")
        self.pushButton_field_45.setFont(font7)
        self.pushButton_field_45.setCheckable(False)
        self.pushButton_field_45.setAutoDefault(False)
        self.pushButton_field_45.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_45, 9, 3, 1, 1)

        self.pushButton_field_57 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_57.setObjectName(u"pushButton_field_57")
        self.pushButton_field_57.setFont(font7)
        self.pushButton_field_57.setCheckable(False)
        self.pushButton_field_57.setAutoDefault(False)
        self.pushButton_field_57.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_57, 9, 4, 1, 1)

        self.pushButton_field_10 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_10.setObjectName(u"pushButton_field_10")
        self.pushButton_field_10.setFont(font7)
        self.pushButton_field_10.setCheckable(False)
        self.pushButton_field_10.setAutoDefault(False)
        self.pushButton_field_10.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_10, 10, 0, 1, 1)

        self.pushButton_field_22 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_22.setObjectName(u"pushButton_field_22")
        self.pushButton_field_22.setFont(font7)
        self.pushButton_field_22.setCheckable(False)
        self.pushButton_field_22.setAutoDefault(False)
        self.pushButton_field_22.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_22, 10, 1, 1, 1)

        self.pushButton_field_34 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_34.setObjectName(u"pushButton_field_34")
        self.pushButton_field_34.setFont(font7)
        self.pushButton_field_34.setCheckable(False)
        self.pushButton_field_34.setAutoDefault(False)
        self.pushButton_field_34.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_34, 10, 2, 1, 1)

        self.pushButton_field_46 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_46.setObjectName(u"pushButton_field_46")
        self.pushButton_field_46.setFont(font7)
        self.pushButton_field_46.setCheckable(False)
        self.pushButton_field_46.setAutoDefault(False)
        self.pushButton_field_46.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_46, 10, 3, 1, 1)

        self.pushButton_field_58 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_58.setObjectName(u"pushButton_field_58")
        self.pushButton_field_58.setFont(font7)
        self.pushButton_field_58.setCheckable(False)
        self.pushButton_field_58.setAutoDefault(False)
        self.pushButton_field_58.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_58, 10, 4, 1, 1)

        self.pushButton_field_11 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_11.setObjectName(u"pushButton_field_11")
        self.pushButton_field_11.setFont(font7)
        self.pushButton_field_11.setCheckable(False)
        self.pushButton_field_11.setAutoDefault(False)
        self.pushButton_field_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_11, 11, 0, 1, 1)

        self.pushButton_field_23 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_23.setObjectName(u"pushButton_field_23")
        self.pushButton_field_23.setFont(font7)
        self.pushButton_field_23.setCheckable(False)
        self.pushButton_field_23.setAutoDefault(False)
        self.pushButton_field_23.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_23, 11, 1, 1, 1)

        self.pushButton_field_35 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_35.setObjectName(u"pushButton_field_35")
        self.pushButton_field_35.setFont(font7)
        self.pushButton_field_35.setCheckable(False)
        self.pushButton_field_35.setAutoDefault(False)
        self.pushButton_field_35.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_35, 11, 2, 1, 1)

        self.pushButton_field_47 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_47.setObjectName(u"pushButton_field_47")
        self.pushButton_field_47.setFont(font7)
        self.pushButton_field_47.setCheckable(False)
        self.pushButton_field_47.setAutoDefault(False)
        self.pushButton_field_47.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_47, 11, 3, 1, 1)

        self.pushButton_field_59 = QPushButton(self.gridLayout_inpallets_table)
        self.pushButton_field_59.setObjectName(u"pushButton_field_59")
        self.pushButton_field_59.setFont(font7)
        self.pushButton_field_59.setCheckable(False)
        self.pushButton_field_59.setAutoDefault(False)
        self.pushButton_field_59.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_field_59, 11, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.gridLayout_inpallets_table)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.pushButton_info = QPushButton(self.centralwidget)
        self.pushButton_info.setObjectName(u"pushButton_info")
        icon3 = QIcon()
        icon3.addFile(u":/icons/help_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_info.setIcon(icon3)
        self.pushButton_info.setIconSize(QSize(40, 40))
        self.pushButton_info.setCheckable(False)
        self.pushButton_info.setAutoRepeat(False)
        self.pushButton_info.setAutoExclusive(False)
        self.pushButton_info.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_info)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_field_0.setDefault(False)
        self.pushButton_field_12.setDefault(False)
        self.pushButton_field_24.setDefault(False)
        self.pushButton_field_36.setDefault(False)
        self.pushButton_field_48.setDefault(False)
        self.pushButton_field_1.setDefault(False)
        self.pushButton_field_13.setDefault(False)
        self.pushButton_field_25.setDefault(False)
        self.pushButton_field_37.setDefault(False)
        self.pushButton_field_49.setDefault(False)
        self.pushButton_field_2.setDefault(False)
        self.pushButton_field_14.setDefault(False)
        self.pushButton_field_26.setDefault(False)
        self.pushButton_field_38.setDefault(False)
        self.pushButton_field_50.setDefault(False)
        self.pushButton_field_3.setDefault(False)
        self.pushButton_field_15.setDefault(False)
        self.pushButton_field_27.setDefault(False)
        self.pushButton_field_39.setDefault(False)
        self.pushButton_field_51.setDefault(False)
        self.pushButton_field_4.setDefault(False)
        self.pushButton_field_16.setDefault(False)
        self.pushButton_field_28.setDefault(False)
        self.pushButton_field_40.setDefault(False)
        self.pushButton_field_52.setDefault(False)
        self.pushButton_field_5.setDefault(False)
        self.pushButton_field_17.setDefault(False)
        self.pushButton_field_29.setDefault(False)
        self.pushButton_field_41.setDefault(False)
        self.pushButton_field_53.setDefault(False)
        self.pushButton_field_6.setDefault(False)
        self.pushButton_field_18.setDefault(False)
        self.pushButton_field_30.setDefault(False)
        self.pushButton_field_42.setDefault(False)
        self.pushButton_field_54.setDefault(False)
        self.pushButton_field_7.setDefault(False)
        self.pushButton_field_19.setDefault(False)
        self.pushButton_field_31.setDefault(False)
        self.pushButton_field_43.setDefault(False)
        self.pushButton_field_55.setDefault(False)
        self.pushButton_field_8.setDefault(False)
        self.pushButton_field_20.setDefault(False)
        self.pushButton_field_32.setDefault(False)
        self.pushButton_field_44.setDefault(False)
        self.pushButton_field_56.setDefault(False)
        self.pushButton_field_9.setDefault(False)
        self.pushButton_field_21.setDefault(False)
        self.pushButton_field_33.setDefault(False)
        self.pushButton_field_45.setDefault(False)
        self.pushButton_field_57.setDefault(False)
        self.pushButton_field_10.setDefault(False)
        self.pushButton_field_22.setDefault(False)
        self.pushButton_field_34.setDefault(False)
        self.pushButton_field_46.setDefault(False)
        self.pushButton_field_58.setDefault(False)
        self.pushButton_field_11.setDefault(False)
        self.pushButton_field_23.setDefault(False)
        self.pushButton_field_35.setDefault(False)
        self.pushButton_field_47.setDefault(False)
        self.pushButton_field_59.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u043b\u043b\u0435\u0442\u043e\u0432 TCL", None))
        self.groupBox_Flashing.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043b\u0435\u0442:", None))
        self.label.setText("")
        self.label_pallet_name.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.label_all_places.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043c\u0435\u0441\u0442: 36", None))
        self.label_last_places.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043c\u0435\u0441\u0442: 2", None))
        self.pushButton_set_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u043b\u043b\u0435\u0442", None))
        self.pushButton_set_complete.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u0430\u043b\u043b\u0435\u0442", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434:", None))
        self.label_leinfo.setText(QCoreApplication.translate("MainWindow", u"SN TV \u0438\u043b\u0438 \u043f\u0430\u043b\u043b\u0435\u0442\u0430:", None))
        self.gridLayout_inpallets_table.setTitle(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0430\u043b\u043b\u0435\u0442\u0435 \u0443\u0436\u0435:", None))
        self.pushButton_field_0.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_12.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_24.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_36.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_48.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_1.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_13.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_25.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_37.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_49.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_2.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_14.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_26.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_38.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_50.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_3.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_15.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_27.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_39.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_51.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_4.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_16.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_28.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_40.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_52.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_5.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_17.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_29.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_41.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_53.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_6.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_18.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_30.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_42.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_54.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_7.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_19.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_31.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_43.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_55.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_8.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_20.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_32.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_44.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_56.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_9.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_21.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_33.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_45.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_57.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_10.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_22.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_34.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_46.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_58.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_11.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_23.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_35.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_47.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_field_59.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_info.setText("")
    # retranslateUi

