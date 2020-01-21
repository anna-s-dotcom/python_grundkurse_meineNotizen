import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QCheckBox, QButtonGroup, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox,QCheckBox, QLabel,QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__ (self):
        super().__init__()
        #QWidget.__init__(self)
        self.resize(640,480)
        self.setWindowTitle("Widget Demo")



    #QApplication?
#setLayout


    #########QPush Button - Schaltfläche####################
        self.schaltflaeche_Button=QPushButton("Schaltfläche")

###########Combo Button - Option 1###########################

        self.combo=QComboBox()
        self.combo.addItem("Option1")


    ###########Q Label - Das ist ein Label ################

        self.label_line=QLabel("Das ist ein Label")
        self.line=QLineEdit()
        self.line=QLineEdit()


##########Check Box ######################

        self.cb1=QCheckBox("Check1")
        self.cb2=QCheckBox("Check2")
        self.cb3=QCheckBox("Check3")


#######Layout################
        v1=QVBoxLayout()
        v1.addWidget(self.combo)
        v1.addWidget(self.cb1s)


        self.setLayout(main)
        self.show()












#programmaufruf
#setstylesheet

STYLE="""
QWidget{
    background:black
}

QComboBox{
    color:red
}
"""

app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
