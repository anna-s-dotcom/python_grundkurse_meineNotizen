import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,QRadioButton, QButtonGroup, QLabel)


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("Button")

        self.label=QLabel()

        self.rb1=QRadioButton("Radio1")
        self.rb2=QRadioButton("Radio2")
        self.rb3=QRadioButton("Radio3")

        self.group=QButtonGroup()
        self.group.addButton(self.rb1)
        self.group.addButton(self.rb2)
        self.group.addButton(self.rb3)

        self.group.buttonClicked.connect(self.change)


        vBox=QVBoxLayout()
        vBox.addWidget(self.rb1)
        vBox.addWidget(self.rb2)
        vBox.addWidget(self.rb3)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def change(self):
        if self.rb1.isChecked():
            self.label.setText("erster")
        elif self.rb1.isChecked():
            self.label.setText("zweiter")
        elif self.rb1.isChecked():
            self.label.setText("dritter")



app=QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())
