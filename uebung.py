import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QComboBox,QVBoxLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout,QTextEdit)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("Zahlenfeld")

        self.line=QLineEdit()
        self.line.setPlaceholderText("Insert Number")
        self.QPushButton("Add from Line")
        self.label=QLabel("10")

        self.value=10
        self.button.clicked.connect(self.change)

        vBox=QVBoxLayout()
        vBo
