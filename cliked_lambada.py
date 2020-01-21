import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout,QTextEdit)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("PlusMinus")


        self.x=0

        self.label=QLabel(f"{self.x}")

        self.plus=QPushButton("Plus5")
        self.minus=QPushButton("Minus 5")

        self.plus.clicked.connect(lambda: self.calc(5))
        self.minus.clicked.connect(lambda: self.calc(-5))


        vBox=QVBoxLayout()

        vBox.addWidget(self.plus)
        vBox.addWidget(self.minus)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def calc(self,value):
        self.x +=value
        self.label.setText(f"{self.x}")
app=QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())
