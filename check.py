import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QButtonGroup


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox")

        #QtWidgets
        self.cb1=QCheckBox("Check1")
        self.cb2=QCheckBox("Check2")
        self.cb3=QCheckBox("Check3")
        self.cb4=QCheckBox("Check4")



        vBox=QVBoxLayout()
        vBox.addWidget(self.cb1)
        vBox.addWidget(self.cb2)
        vBox.addWidget(self.cb3)
        vBox.addWidget(self.cb4)

    

        self.setLayout(vBox)
        self.show()

app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
