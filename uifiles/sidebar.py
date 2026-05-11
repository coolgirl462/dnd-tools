from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("DnDMenu")

        self.DiceRollerPB1.clicked.connect(self.switch_to_dicerollerpage)
        self.DiceRollerPB2.clicked.connect(self.switch_to_dicerollerpage)

        self.CharacterPB1.clicked.connect(self.switch_to_characterpage)
        self.CharacterPB1.clicked.connect(self.switch_to_characterpage)

        self.ProfilePB1.clicked.connect(self.switch_to_profilepage)
        self.ProfilePB2.clicked.connect(self.switch_to_profilepage)

        self.iconnamewidget.setHidden(True)



    def switch_to_dicerollerpage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_characterpage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_profilepage(self):
        self.stackedWidget.setCurrentIndex(2)


