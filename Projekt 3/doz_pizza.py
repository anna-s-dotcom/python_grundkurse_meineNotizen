import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QCheckBox, QLabel, QTextEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("Pizza Bestellung")

        # Widgets
        self.preis = 6
        # Alle Label definieren
        self.grLabel = QLabel("Größe der Pizza")
        self.zutLabel = QLabel("Was soll drauf?")
        self.extraLabel = QLabel("Sonderwünsche: ")


        # Radiobuttons definiert und gruppiert
        self.gRadio = QRadioButton("Groß")
        self.gRadio.setChecked(True)
        self.mRadio = QRadioButton("Mittel")
        self.kRadio = QRadioButton("Klein")
        self.size = QButtonGroup()
        self.size.addButton(self.gRadio)
        self.size.addButton(self.mRadio)
        self.size.addButton(self.kRadio)
        self.preisLabel = QLabel(f"Der Preis ist {self.preis}")

        self.size.buttonClicked.connect(self.price)

        # checkboxen definieren
        self.tomate = QCheckBox("Tomate")
        self.tomate.clicked.connect(self.price)
        self.bacon = QCheckBox("Bacon")
        self.bacon.clicked.connect(self.price)
        self.salami = QCheckBox("Salami")
        self.salami.clicked.connect(self.price)
        self.cheese = QCheckBox("Käse")
        self.cheese.clicked.connect(self.price)
        self.chili = QCheckBox("Chili")
        self.chili.clicked.connect(self.price)
        self.pilze = QCheckBox("Pilze")
        self.pilze.clicked.connect(self.price)

        # Textfeld
        self.extraText = QTextEdit()

        # Layout

        rahmen = QVBoxLayout()

        grLayout = QHBoxLayout()
        grLayout.addWidget(self.gRadio)
        grLayout.addWidget(self.mRadio)
        grLayout.addWidget(self.kRadio)

        zutLayout = QGridLayout()
        zutLayout.addWidget(self.tomate, 0, 0)
        zutLayout.addWidget(self.bacon, 0 ,1)
        zutLayout.addWidget(self.salami, 0 , 2)
        zutLayout.addWidget(self.cheese, 1, 0)
        zutLayout.addWidget(self.chili, 1 , 1)
        zutLayout.addWidget(self.pilze, 1, 2)


        rahmen.addWidget(self.grLabel)
        rahmen.addLayout(grLayout)
        rahmen.addWidget(self.zutLabel)
        rahmen.addLayout(zutLayout)
        rahmen.addWidget(self.extraLabel)
        rahmen.addWidget(self.extraText)
        rahmen.addWidget(self.preisLabel)

        self.setLayout(rahmen)
        self.show()

    def price(self):
        # print(self.size.checkedButton().text())
        if self.gRadio.isChecked():
            self.preis = 6
        elif self.mRadio.isChecked():
            self.preis = 4
        elif self.kRadio.isChecked():
            self.preis = 2

        if self.tomate.isChecked():
            self.preis += 1
        if self.bacon.isChecked():
            self.preis += 1
        if self.cheese.isChecked():
            self.preis += 1
        if self.chili.isChecked():
            self.preis += 1
        if self.salami.isChecked():
            self.preis += 1
        if self.pilze.isChecked():
            self.preis += 1

        self.preisLabel.setText(f"Der Preis ist {self.preis:.2f}€")
STYLE = """
Window{
    background: grey
    }
QWidget{
    color: white
    }
QLabel{
    color: blue;
    font-size: 16px;
    font-weight: bold;
    }
QTextEdit{
    background: black
    }
"""

#Hauptprogramm
app = QApplication(sys.argv)
app.setStyleSheet(STYLE)
w = Window()

sys.exit(app.exec_())
