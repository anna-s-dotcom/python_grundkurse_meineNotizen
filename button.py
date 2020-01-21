import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.setWindowTitle("Button Horizontal")


        #Widgets
        self.okButton=QPushButton("OK")
        self.cancelButton=QPushButton("Cancel")

        #horizontales QHBoxLayout

        hbox=QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)


        self.setLayout(hbox)

        self.show()

#programmaufruf
app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
