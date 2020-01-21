import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout
from PyQt5.QtWidgets import QLineEdit, QTextEdit,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowTitle("Combobox")

        self.label_line=QLabel("Label for Line")
        self.label_text=QLabel("Label for Text")

        self.line=QLineEdit()
        self.text=QTextEdit()


        vBox=QVBoxLayout()
        vBox.addWidget(self.label_line)
        vBox.addWidget(self.line)
        vBox.addWidget(self.label_text)
        vBox.addWidget(self.text)

        self.setLayout(vBox)
        self.show()



app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
