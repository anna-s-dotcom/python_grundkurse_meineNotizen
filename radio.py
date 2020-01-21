import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowTitle("Radio Button")


        #QtWidgets

        self.rb1=QRadioButton("Button1")
        self.rb2=QRadioButton("Button2")
        self.rb3=QRadioButton("Button3")
        self.rb4=QRadioButton("Button4")
        self.rb5=QRadioButton("Button6")

        self.group1=QButtonGroup()
        self.group1.addButton(self.rb1)
        self.group1.addButton(self.rb2)
        self.group1.addButton(self.rb3)

        self.group2=QButtonGroup()
        self.group2.addButton(self.rb4)
        self.group2.addButton(self.rb5)


        vBox=QVBoxLayout()
        vBox.addWidget(self.rb1)
        vBox.addWidget(self.rb2)
        vBox.addWidget(self.rb3)
        vBox.addWidget(self.rb4)
        vBox.addWidget(self.rb5)


        self.setLayout(vBox)
        self.show()

app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
