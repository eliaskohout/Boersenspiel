"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.DATEN as D

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


def main():
    spieler = S.SPIELER('Bob')

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.daten = D.DATEN()
        self.daten.tickerErneuern()
        self.daten.tickers.saveToFile()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Hier können die Methoden mit den Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen

    def suche(self):
        self.ui.listWidget_suchergebnis.clear()
        phrase = self.ui.plainTextEdit_aktiensuche.toPlainText()
        liste = ["{} ({})".format(e[0], e[1]) for e in self.daten.tickers.inhaltSuchen(phrase)]
        self.ui.listWidget_suchergebnis.addItems(liste)


if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()
