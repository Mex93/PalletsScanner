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
        MainWindow.resize(907, 826)
        icon = QIcon()
        icon.addFile(u":/images/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/pallet_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.label_pallet_name = QLabel(self.groupBox)
        self.label_pallet_name.setObjectName(u"label_pallet_name")
        font1 = QFont()
        font1.setPointSize(25)
        self.label_pallet_name.setFont(font1)
#if QT_CONFIG(tooltip)
        self.label_pallet_name.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_pallet_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
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
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_all_places = QLabel(self.groupBox)
        self.label_all_places.setObjectName(u"label_all_places")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setUnderline(True)
        self.label_all_places.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_all_places)

        self.label_last_places = QLabel(self.groupBox)
        self.label_last_places.setObjectName(u"label_last_places")
        self.label_last_places.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_last_places)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_set_cancel = QPushButton(self.groupBox)
        self.pushButton_set_cancel.setObjectName(u"pushButton_set_cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_set_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_set_cancel.setSizePolicy(sizePolicy)
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_set_complete = QPushButton(self.groupBox)
        self.pushButton_set_complete.setObjectName(u"pushButton_set_complete")
        sizePolicy.setHeightForWidth(self.pushButton_set_complete.sizePolicy().hasHeightForWidth())
        self.pushButton_set_complete.setSizePolicy(sizePolicy)
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


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_main.sizePolicy().hasHeightForWidth())
        self.le_main.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.le_main.setFont(font5)
        self.le_main.setInputMask(u"")
        self.le_main.setText(u"")
        self.le_main.setMaxLength(15)
        self.le_main.setFrame(True)
        self.le_main.setEchoMode(QLineEdit.EchoMode.Normal)
        self.le_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_main.setDragEnabled(False)
        self.le_main.setPlaceholderText(u"")
        self.le_main.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_main)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setUnderline(False)
        self.groupBox_2.setFont(font6)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_inpallets_table = QGridLayout()
        self.gridLayout_inpallets_table.setObjectName(u"gridLayout_inpallets_table")
        self.labeL_in_pall_0 = QLabel(self.groupBox_2)
        self.labeL_in_pall_0.setObjectName(u"labeL_in_pall_0")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setUnderline(False)
        self.labeL_in_pall_0.setFont(font7)
        self.labeL_in_pall_0.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_0.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_0.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_0, 0, 0, 1, 1)

        self.labeL_in_pall_9 = QLabel(self.groupBox_2)
        self.labeL_in_pall_9.setObjectName(u"labeL_in_pall_9")
        self.labeL_in_pall_9.setFont(font7)
        self.labeL_in_pall_9.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_9.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_9.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_9, 0, 1, 1, 1)

        self.labeL_in_pall_18 = QLabel(self.groupBox_2)
        self.labeL_in_pall_18.setObjectName(u"labeL_in_pall_18")
        self.labeL_in_pall_18.setFont(font7)
        self.labeL_in_pall_18.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_18.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_18.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_18, 0, 2, 1, 1)

        self.labeL_in_pall_27 = QLabel(self.groupBox_2)
        self.labeL_in_pall_27.setObjectName(u"labeL_in_pall_27")
        self.labeL_in_pall_27.setFont(font7)
        self.labeL_in_pall_27.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_27.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_27.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_27, 0, 3, 1, 1)

        self.labeL_in_pall_1 = QLabel(self.groupBox_2)
        self.labeL_in_pall_1.setObjectName(u"labeL_in_pall_1")
        self.labeL_in_pall_1.setFont(font7)
        self.labeL_in_pall_1.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_1.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_1.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_1, 1, 0, 1, 1)

        self.labeL_in_pall_10 = QLabel(self.groupBox_2)
        self.labeL_in_pall_10.setObjectName(u"labeL_in_pall_10")
        self.labeL_in_pall_10.setFont(font7)
        self.labeL_in_pall_10.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_10.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_10.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_10, 1, 1, 1, 1)

        self.labeL_in_pall_19 = QLabel(self.groupBox_2)
        self.labeL_in_pall_19.setObjectName(u"labeL_in_pall_19")
        self.labeL_in_pall_19.setFont(font7)
        self.labeL_in_pall_19.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_19.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_19.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_19, 1, 2, 1, 1)

        self.labeL_in_pall_28 = QLabel(self.groupBox_2)
        self.labeL_in_pall_28.setObjectName(u"labeL_in_pall_28")
        self.labeL_in_pall_28.setFont(font7)
        self.labeL_in_pall_28.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_28.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_28.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_28, 1, 3, 1, 1)

        self.labeL_in_pall_2 = QLabel(self.groupBox_2)
        self.labeL_in_pall_2.setObjectName(u"labeL_in_pall_2")
        self.labeL_in_pall_2.setFont(font7)
        self.labeL_in_pall_2.setStyleSheet(u"")
        self.labeL_in_pall_2.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_2.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_2.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_2, 2, 0, 1, 1)

        self.labeL_in_pall_11 = QLabel(self.groupBox_2)
        self.labeL_in_pall_11.setObjectName(u"labeL_in_pall_11")
        self.labeL_in_pall_11.setFont(font7)
        self.labeL_in_pall_11.setStyleSheet(u"")
        self.labeL_in_pall_11.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_11.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_11.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_11, 2, 1, 1, 1)

        self.labeL_in_pall_20 = QLabel(self.groupBox_2)
        self.labeL_in_pall_20.setObjectName(u"labeL_in_pall_20")
        self.labeL_in_pall_20.setFont(font7)
        self.labeL_in_pall_20.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_20.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_20.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_20, 2, 2, 1, 1)

        self.labeL_in_pall_29 = QLabel(self.groupBox_2)
        self.labeL_in_pall_29.setObjectName(u"labeL_in_pall_29")
        self.labeL_in_pall_29.setFont(font7)
        self.labeL_in_pall_29.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_29.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_29.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_29, 2, 3, 1, 1)

        self.labeL_in_pall_3 = QLabel(self.groupBox_2)
        self.labeL_in_pall_3.setObjectName(u"labeL_in_pall_3")
        self.labeL_in_pall_3.setFont(font7)
        self.labeL_in_pall_3.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_3.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_3.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_3, 3, 0, 1, 1)

        self.labeL_in_pall_12 = QLabel(self.groupBox_2)
        self.labeL_in_pall_12.setObjectName(u"labeL_in_pall_12")
        self.labeL_in_pall_12.setFont(font7)
        self.labeL_in_pall_12.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_12.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_12.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_12, 3, 1, 1, 1)

        self.labeL_in_pall_21 = QLabel(self.groupBox_2)
        self.labeL_in_pall_21.setObjectName(u"labeL_in_pall_21")
        self.labeL_in_pall_21.setFont(font7)
        self.labeL_in_pall_21.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_21.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_21.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_21, 3, 2, 1, 1)

        self.labeL_in_pall_30 = QLabel(self.groupBox_2)
        self.labeL_in_pall_30.setObjectName(u"labeL_in_pall_30")
        self.labeL_in_pall_30.setFont(font7)
        self.labeL_in_pall_30.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_30.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_30.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_30, 3, 3, 1, 1)

        self.labeL_in_pall_4 = QLabel(self.groupBox_2)
        self.labeL_in_pall_4.setObjectName(u"labeL_in_pall_4")
        self.labeL_in_pall_4.setFont(font7)
        self.labeL_in_pall_4.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_4.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_4.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_4, 4, 0, 1, 1)

        self.labeL_in_pall_13 = QLabel(self.groupBox_2)
        self.labeL_in_pall_13.setObjectName(u"labeL_in_pall_13")
        self.labeL_in_pall_13.setFont(font7)
        self.labeL_in_pall_13.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_13.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_13.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_13, 4, 1, 1, 1)

        self.labeL_in_pall_22 = QLabel(self.groupBox_2)
        self.labeL_in_pall_22.setObjectName(u"labeL_in_pall_22")
        self.labeL_in_pall_22.setFont(font7)
        self.labeL_in_pall_22.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_22.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_22.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_22, 4, 2, 1, 1)

        self.labeL_in_pall_31 = QLabel(self.groupBox_2)
        self.labeL_in_pall_31.setObjectName(u"labeL_in_pall_31")
        self.labeL_in_pall_31.setFont(font7)
        self.labeL_in_pall_31.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_31.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_31.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_31, 4, 3, 1, 1)

        self.labeL_in_pall_5 = QLabel(self.groupBox_2)
        self.labeL_in_pall_5.setObjectName(u"labeL_in_pall_5")
        self.labeL_in_pall_5.setFont(font7)
        self.labeL_in_pall_5.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_5.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_5.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_5, 5, 0, 1, 1)

        self.labeL_in_pall_14 = QLabel(self.groupBox_2)
        self.labeL_in_pall_14.setObjectName(u"labeL_in_pall_14")
        self.labeL_in_pall_14.setFont(font7)
        self.labeL_in_pall_14.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_14.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_14.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_14, 5, 1, 1, 1)

        self.labeL_in_pall_23 = QLabel(self.groupBox_2)
        self.labeL_in_pall_23.setObjectName(u"labeL_in_pall_23")
        self.labeL_in_pall_23.setFont(font7)
        self.labeL_in_pall_23.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_23.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_23.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_23, 5, 2, 1, 1)

        self.labeL_in_pall_32 = QLabel(self.groupBox_2)
        self.labeL_in_pall_32.setObjectName(u"labeL_in_pall_32")
        self.labeL_in_pall_32.setFont(font7)
        self.labeL_in_pall_32.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_32.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_32.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_32, 5, 3, 1, 1)

        self.labeL_in_pall_6 = QLabel(self.groupBox_2)
        self.labeL_in_pall_6.setObjectName(u"labeL_in_pall_6")
        self.labeL_in_pall_6.setFont(font7)
        self.labeL_in_pall_6.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_6.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_6.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_6, 6, 0, 1, 1)

        self.labeL_in_pall_15 = QLabel(self.groupBox_2)
        self.labeL_in_pall_15.setObjectName(u"labeL_in_pall_15")
        self.labeL_in_pall_15.setFont(font7)
        self.labeL_in_pall_15.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_15.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_15.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_15, 6, 1, 1, 1)

        self.labeL_in_pall_24 = QLabel(self.groupBox_2)
        self.labeL_in_pall_24.setObjectName(u"labeL_in_pall_24")
        self.labeL_in_pall_24.setFont(font7)
        self.labeL_in_pall_24.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_24.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_24.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_24, 6, 2, 1, 1)

        self.labeL_in_pall_33 = QLabel(self.groupBox_2)
        self.labeL_in_pall_33.setObjectName(u"labeL_in_pall_33")
        self.labeL_in_pall_33.setFont(font7)
        self.labeL_in_pall_33.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_33.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_33.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_33, 6, 3, 1, 1)

        self.labeL_in_pall_7 = QLabel(self.groupBox_2)
        self.labeL_in_pall_7.setObjectName(u"labeL_in_pall_7")
        self.labeL_in_pall_7.setFont(font7)
        self.labeL_in_pall_7.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_7.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_7.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_7, 7, 0, 1, 1)

        self.labeL_in_pall_16 = QLabel(self.groupBox_2)
        self.labeL_in_pall_16.setObjectName(u"labeL_in_pall_16")
        self.labeL_in_pall_16.setFont(font7)
        self.labeL_in_pall_16.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_16.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_16.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_16, 7, 1, 1, 1)

        self.labeL_in_pall_25 = QLabel(self.groupBox_2)
        self.labeL_in_pall_25.setObjectName(u"labeL_in_pall_25")
        self.labeL_in_pall_25.setFont(font7)
        self.labeL_in_pall_25.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_25.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_25.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_25, 7, 2, 1, 1)

        self.labeL_in_pall_34 = QLabel(self.groupBox_2)
        self.labeL_in_pall_34.setObjectName(u"labeL_in_pall_34")
        self.labeL_in_pall_34.setFont(font7)
        self.labeL_in_pall_34.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_34.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_34.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_34, 7, 3, 1, 1)

        self.labeL_in_pall_8 = QLabel(self.groupBox_2)
        self.labeL_in_pall_8.setObjectName(u"labeL_in_pall_8")
        self.labeL_in_pall_8.setFont(font7)
        self.labeL_in_pall_8.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_8.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_8.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_8, 8, 0, 1, 1)

        self.labeL_in_pall_17 = QLabel(self.groupBox_2)
        self.labeL_in_pall_17.setObjectName(u"labeL_in_pall_17")
        self.labeL_in_pall_17.setFont(font7)
        self.labeL_in_pall_17.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_17.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_17.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_17, 8, 1, 1, 1)

        self.labeL_in_pall_26 = QLabel(self.groupBox_2)
        self.labeL_in_pall_26.setObjectName(u"labeL_in_pall_26")
        self.labeL_in_pall_26.setFont(font7)
        self.labeL_in_pall_26.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_26.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_26.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_26, 8, 2, 1, 1)

        self.labeL_in_pall_35 = QLabel(self.groupBox_2)
        self.labeL_in_pall_35.setObjectName(u"labeL_in_pall_35")
        self.labeL_in_pall_35.setFont(font7)
        self.labeL_in_pall_35.setFrameShape(QFrame.Shape.NoFrame)
        self.labeL_in_pall_35.setFrameShadow(QFrame.Shadow.Plain)
        self.labeL_in_pall_35.setTextFormat(Qt.TextFormat.AutoText)
        self.labeL_in_pall_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_inpallets_table.addWidget(self.labeL_in_pall_35, 8, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_inpallets_table)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.verticalLayout_6.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

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


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u043b\u043b\u0435\u0442\u043e\u0432 TCL", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043b\u0435\u0442:", None))
        self.label.setText("")
        self.label_pallet_name.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.label_all_places.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043c\u0435\u0441\u0442: 36", None))
        self.label_last_places.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043c\u0435\u0441\u0442: 2", None))
        self.pushButton_set_cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u043b\u043b\u0435\u0442", None))
        self.pushButton_set_complete.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u043f\u0430\u043b\u043b\u0435\u0442", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434:", None))
        self.label_leinfo.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 SN \u0438\u043b\u0438 \u043f\u0430\u043b\u043b\u0435\u0442\u0430:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0430\u043b\u043b\u0435\u0442\u0435 \u0443\u0436\u0435:", None))
        self.labeL_in_pall_0.setText(QCoreApplication.translate("MainWindow", u"2404DTF801280900001", None))
        self.labeL_in_pall_9.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_18.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_27.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_1.setText(QCoreApplication.translate("MainWindow", u"2404DTF801280900001", None))
        self.labeL_in_pall_10.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_19.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_28.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0437\u0430\u043d\u044f\u0442\u043e", None))
        self.labeL_in_pall_11.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e", None))
        self.labeL_in_pall_20.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_29.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_3.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_12.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_21.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_30.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_4.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_13.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_22.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_31.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_5.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_14.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_23.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_32.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_6.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_15.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_24.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_33.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_7.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_16.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_25.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_34.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_8.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_17.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_26.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.labeL_in_pall_35.setText(QCoreApplication.translate("MainWindow", u"2404BCF207460C00001", None))
        self.pushButton_info.setText("")
    # retranslateUi

