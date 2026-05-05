import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

class MainUi(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.button = QtWidgets.QPushButton("Click me!")
		self.Roll_Count = QtWidgets.QLineEdit()
		self.Dice_Type = QtWidgets.QLineEdit()
		self.text = QtWidgets.QLabel("Hello World")

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.Roll_Count)
		self.layout.addWidget(self.Dice_Type)

		self.button.clicked.connect(self.magic)

	@QtCore.Slot()
	def magic(self):
		result = roll(int(self.Roll_Count.text()), int(self.Dice_Type.text()))
		
		self.text.setText(str(result))
		

def roll(roll_count, dice_type):
	sum = 0 
	for i in range(1,roll_count+1):
		roll_result = random.randint(1,dice_type)
		print(roll_result)
		sum += roll_result

	return sum

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	widget = MainUi()
	widget.resize(800, 600)
	widget.show()

	print(widget.text.text())

	sys.exit(app.exec())
