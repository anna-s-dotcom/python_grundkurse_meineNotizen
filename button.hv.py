import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowTitle("Button Horizontal/Vertical")

        #Widgets

        self.ok1=QPushButton("OK 1")
        self.can1=QPushButton("Cancel 1")
        self.ok2=QPushButton("OK 2")
        self.can2=QPushButton("Cancel 2")
        self.ok3=QPushButton("OK 3")
        self.can3=QPushButton("Cancel 3")
        self.ok4=QPushButton("OK 4")
        self.can4=QPushButton("Cancel 4")


        #setLayout

#         vBox=QVBoxLayout()
#         vBox.addWidget(self.ok1)
#         vBox.addWidget(self.can1)
# #hier durch QV die vertikale position ändern
#         hBox=QVBoxLayout()
#         hBox.addWidget(self.ok2)
#         hBox.addWidget(self.can2)
#
#         main=QVBoxLayout()
#         main.addLayout(vBox)
#         main.addLayout(hBox)
#
        main=QGridLayout()
        main.addWidget(self.ok1, 0,0)
        main.addWidget(self.can1, 1,1)
        main.addWidget(self.ok2, 2,2)
        main.addWidget(self.can2, 3,3)
        main.addWidget(self.ok3, 4,4)
        main.addWidget(self.can3, 5,5)



        self.setLayout(main)
        self.show()


app=QApplication(sys.argv)
w=Window()

sys.exit(app.exec_())
