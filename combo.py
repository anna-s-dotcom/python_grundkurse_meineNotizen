import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout,QComboBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowTitle("Combobox")


        self.combo=QComboBox()
        self.combo.addItem("Item 1")
        self.combo.addItem("Item 2")
        self.combo.addItem("Item 3")
        self.combo.addItem("Item 4")


        vBox=QVBoxLayout()
        vBox.addWidget(self.combo)
        
        self.setLayout(vBox)
        self.show()

app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
