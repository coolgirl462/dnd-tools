# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(397, 325)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 201, 202);\n"
"align:left")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.icononlywidget = QWidget(self.centralwidget)
        self.icononlywidget.setObjectName(u"icononlywidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icononlywidget.sizePolicy().hasHeightForWidth())
        self.icononlywidget.setSizePolicy(sizePolicy)
        self.icononlywidget.setMinimumSize(QSize(67, 313))
        self.icononlywidget.setMaximumSize(QSize(67, 1000))
        self.icononlywidget.setStyleSheet(u"QWidget{background-color: qlineargradient(spread:pad, x1:0.452514, y1:0.011, x2:0.52514, y2:1, stop:0 rgba(219, 25, 90, 255), stop:1 rgba(255, 176, 119, 255));\n"
"\n"
"}\n"
"QPushButton{\n"
"height:30px;\n"
"border:none;\n"
"background-color: transparent\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"font-weight:bold;\n"
"color:red;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.icononlywidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.icononlywidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"background-color:transparent\n"
"")
        self.label_7.setPixmap(QPixmap(u":/newPrefix/imageswithbackground/admin-removebg-preview.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setMargin(0)
        self.label_7.setIndent(0)

        self.verticalLayout.addWidget(self.label_7)

        self.WidgetPB1 = QPushButton(self.icononlywidget)
        self.WidgetPB1.setObjectName(u"WidgetPB1")
        icon = QIcon()
        icon.addFile(u":/newPrefix/imageswithbackground/widget.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WidgetPB1.setIcon(icon)
        self.WidgetPB1.setIconSize(QSize(18, 18))
        self.WidgetPB1.setCheckable(True)
        self.WidgetPB1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.WidgetPB1)

        self.DiceRollerPB1 = QPushButton(self.icononlywidget)
        self.DiceRollerPB1.setObjectName(u"DiceRollerPB1")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/imageswithbackground/diceroll.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DiceRollerPB1.setIcon(icon1)
        self.DiceRollerPB1.setIconSize(QSize(18, 18))
        self.DiceRollerPB1.setCheckable(True)
        self.DiceRollerPB1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.DiceRollerPB1)

        self.CharacterPB1 = QPushButton(self.icononlywidget)
        self.CharacterPB1.setObjectName(u"CharacterPB1")
        self.CharacterPB1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/imageswithbackground/character.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CharacterPB1.setIcon(icon2)
        self.CharacterPB1.setIconSize(QSize(18, 18))
        self.CharacterPB1.setCheckable(True)
        self.CharacterPB1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.CharacterPB1)

        self.ProfilePB1 = QPushButton(self.icononlywidget)
        self.ProfilePB1.setObjectName(u"ProfilePB1")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/imageswithbackground/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ProfilePB1.setIcon(icon3)
        self.ProfilePB1.setIconSize(QSize(18, 18))
        self.ProfilePB1.setCheckable(True)
        self.ProfilePB1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ProfilePB1)

        self.verticalSpacer_2 = QSpacerItem(20, 771, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.ExitPB1 = QPushButton(self.icononlywidget)
        self.ExitPB1.setObjectName(u"ExitPB1")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/imageswithbackground/exit button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExitPB1.setIcon(icon4)
        self.ExitPB1.setIconSize(QSize(18, 18))
        self.ExitPB1.setCheckable(True)
        self.ExitPB1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ExitPB1)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.icononlywidget, 0, 0, 1, 1)

        self.iconnamewidget = QWidget(self.centralwidget)
        self.iconnamewidget.setObjectName(u"iconnamewidget")
        sizePolicy.setHeightForWidth(self.iconnamewidget.sizePolicy().hasHeightForWidth())
        self.iconnamewidget.setSizePolicy(sizePolicy)
        self.iconnamewidget.setMinimumSize(QSize(117, 313))
        self.iconnamewidget.setMaximumSize(QSize(169, 1000))
        self.iconnamewidget.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.452514, y1:0.011, x2:0.52514, y2:1, stop:0 rgba(219, 25, 90, 255), stop:1 rgba(255, 176, 119, 255));\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"\n"
"}\n"
"QPushButton{\n"
"height:30px;\n"
"border:none;\n"
"background-color:transparent\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"font-weight:bold;\n"
"color:red;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}")
        self.gridLayout = QGridLayout(self.iconnamewidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.iconnamewidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setStyleSheet(u"background-color: transparent;")
        self.label_8.setPixmap(QPixmap(u":/newPrefix/imageswithbackground/admin-removebg-preview.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setMargin(0)
        self.label_8.setIndent(0)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label = QLabel(self.iconnamewidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 8pt \"MS Sans Serif\";\n"
"fontstyle:bold;\n"
"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.WidgetPB2 = QPushButton(self.iconnamewidget)
        self.WidgetPB2.setObjectName(u"WidgetPB2")
        sizePolicy.setHeightForWidth(self.WidgetPB2.sizePolicy().hasHeightForWidth())
        self.WidgetPB2.setSizePolicy(sizePolicy)
        self.WidgetPB2.setStyleSheet(u"")
        self.WidgetPB2.setIcon(icon)
        self.WidgetPB2.setIconSize(QSize(18, 18))
        self.WidgetPB2.setCheckable(True)
        self.WidgetPB2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.WidgetPB2)

        self.DiceRollerPB2 = QPushButton(self.iconnamewidget)
        self.DiceRollerPB2.setObjectName(u"DiceRollerPB2")
        sizePolicy.setHeightForWidth(self.DiceRollerPB2.sizePolicy().hasHeightForWidth())
        self.DiceRollerPB2.setSizePolicy(sizePolicy)
        self.DiceRollerPB2.setStyleSheet(u"")
        self.DiceRollerPB2.setIcon(icon1)
        self.DiceRollerPB2.setIconSize(QSize(18, 18))
        self.DiceRollerPB2.setCheckable(True)
        self.DiceRollerPB2.setChecked(False)
        self.DiceRollerPB2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.DiceRollerPB2)

        self.CharactersPB2 = QPushButton(self.iconnamewidget)
        self.CharactersPB2.setObjectName(u"CharactersPB2")
        sizePolicy.setHeightForWidth(self.CharactersPB2.sizePolicy().hasHeightForWidth())
        self.CharactersPB2.setSizePolicy(sizePolicy)
        self.CharactersPB2.setMinimumSize(QSize(0, 0))
        self.CharactersPB2.setStyleSheet(u"")
        self.CharactersPB2.setIcon(icon2)
        self.CharactersPB2.setIconSize(QSize(18, 18))
        self.CharactersPB2.setCheckable(True)
        self.CharactersPB2.setChecked(False)
        self.CharactersPB2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.CharactersPB2)

        self.ProfilePB2 = QPushButton(self.iconnamewidget)
        self.ProfilePB2.setObjectName(u"ProfilePB2")
        sizePolicy.setHeightForWidth(self.ProfilePB2.sizePolicy().hasHeightForWidth())
        self.ProfilePB2.setSizePolicy(sizePolicy)
        self.ProfilePB2.setMinimumSize(QSize(23, 20))
        self.ProfilePB2.setStyleSheet(u"")
        self.ProfilePB2.setIcon(icon3)
        self.ProfilePB2.setIconSize(QSize(18, 18))
        self.ProfilePB2.setCheckable(True)
        self.ProfilePB2.setChecked(False)
        self.ProfilePB2.setAutoRepeat(False)
        self.ProfilePB2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ProfilePB2)

        self.verticalSpacer_3 = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.ExitPB2 = QPushButton(self.iconnamewidget)
        self.ExitPB2.setObjectName(u"ExitPB2")
        self.ExitPB2.setStyleSheet(u"")
        self.ExitPB2.setIcon(icon4)
        self.ExitPB2.setIconSize(QSize(18, 18))
        self.ExitPB2.setCheckable(True)
        self.ExitPB2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ExitPB2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.iconnamewidget, 0, 1, 1, 1)

        self.mainmenu = QWidget(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.mainmenu.setMaximumSize(QSize(10000, 10000))
        self.mainmenu.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.mainmenu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.mainmenu)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.mainmenu)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/imageswithbackground/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.mainmenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(50000, 50000))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Dicerollerpage = QWidget()
        self.Dicerollerpage.setObjectName(u"Dicerollerpage")
        self.label_2 = QLabel(self.Dicerollerpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 60, 35, 10))
        self.stackedWidget.addWidget(self.Dicerollerpage)
        self.Characterspage = QWidget()
        self.Characterspage.setObjectName(u"Characterspage")
        self.label_3 = QLabel(self.Characterspage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 90, 35, 10))
        self.stackedWidget.addWidget(self.Characterspage)
        self.Profilepage = QWidget()
        self.Profilepage.setObjectName(u"Profilepage")
        self.label_4 = QLabel(self.Profilepage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 80, 35, 10))
        self.stackedWidget.addWidget(self.Profilepage)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.mainmenu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.WidgetPB1.pressed.connect(self.iconnamewidget.show)
        self.WidgetPB2.pressed.connect(self.iconnamewidget.hide)
        self.ProfilePB1.toggled.connect(self.ProfilePB2.setChecked)
        self.CharacterPB1.toggled.connect(self.CharactersPB2.setChecked)
        self.DiceRollerPB1.toggled.connect(self.DiceRollerPB2.setChecked)
        self.ProfilePB2.toggled.connect(self.ProfilePB1.setChecked)
        self.CharactersPB2.toggled.connect(self.CharacterPB1.setChecked)
        self.DiceRollerPB2.toggled.connect(self.DiceRollerPB1.setChecked)
        self.ExitPB1.clicked["bool"].connect(MainWindow.close)
        self.ExitPB2.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.WidgetPB1.setText("")
        self.DiceRollerPB1.setText("")
        self.CharacterPB1.setText("")
        self.ProfilePB1.setText("")
        self.ExitPB1.setText("")
        self.label_8.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.WidgetPB2.setText(QCoreApplication.translate("MainWindow", u"MAKE IT SMALL", None))
        self.DiceRollerPB2.setText(QCoreApplication.translate("MainWindow", u"DICE ROLLER", None))
        self.CharactersPB2.setText(QCoreApplication.translate("MainWindow", u"CHARACTERS", None))
        self.ProfilePB2.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.ExitPB2.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"diceroller", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"character", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

