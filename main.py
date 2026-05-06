import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression


class MainUi(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.button = QtWidgets.QPushButton("Roll!")
		self.Roll_Count = QtWidgets.QLineEdit()
		self.Dice_Type = QtWidgets.QLineEdit()
		self.text = QtWidgets.QLabel("Hello World")
		self.Rolls_Display = QtWidgets.QLabel("Roll results")
	
		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.Roll_Count)
		self.layout.addWidget(self.Dice_Type)
		self.layout.addWidget(self.Rolls_Display)

		validator = QRegularExpressionValidator(QRegularExpression("^[0-9]*$"))
		self.Roll_Count.setValidator(validator)
		self.Dice_Type.setValidator(validator)

		self.Roll_Count.setPlaceholderText("How many die are you rolling?")
		self.Dice_Type.setPlaceholderText("What kinda die are you rolling?")

		self.button.clicked.connect(self.magic)

	@QtCore.Slot()
	def magic(self):
		result,rolls = roll(int(self.Roll_Count.text()), int(self.Dice_Type.text()))
		
		self.text.setText(str(result))
		self.Rolls_Display.setText(str(rolls))

def roll(roll_count, dice_type):
	rolls = []
	sum = 0 
	for i in range(1,roll_count+1):
		roll_result = random.randint(1,dice_type)
		rolls.append(roll_result)
		print(roll_result)	
		sum += roll_result	
	print(rolls)
	return sum,rolls


if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	widget = MainUi()
	widget.resize(800, 600)
	widget.show()
	widget.setWindowTitle("DND Helper") # find me a good name
	widget.setWindowIcon(QIcon('images\dndhelper logo.png'))
	print(widget.text.text())

	sys.exit(app.exec())
