import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QComboBox,QVBoxLayout)

class Window(QWidget):
    def __init__ (self):
        super().__init__()

        self.resize(640,480)
        self.setWindowTitle("Widget Demo")
        self.setWindowTitle("Working Combobox")

            #widget
        self.label=QLabel()
        self.combo=QComboBox()
        self.combo.addItem("Item1")
        self.combo.addItem("Item2")
        self.combo.addItem("Item3")
        self.combo.addItem("Item4")

        #signal, string übergibt in die Methode

        self.combo.activated[str].connect(self.change)


            #setLayout

        vBox=QVBoxLayout()
        vBox.addWidget(self.combo)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def change(self,str):
        self.label.setText(string)



app=QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())
