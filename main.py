"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.DATEN as D

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


def main():
    pass

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spieler = S.SPIELER('Bob')
        self.daten = D.DATEN()
        self.aktuellerticker=""
        self.daten.tickers.saveToFile()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tabWidget.setTabVisible(3, False)

        # Hier können die Methoden mit den Signalen der Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)
        self.ui.listWidget_suchergebnis.itemDoubleClicked.connect(self.launchAktieninfo)
        self.ui.pushButton_kaufen.clicked.connect(self.kaufenclick)
        #print(str(self.ui.spinBox_anzahlKaufen.text()))
        self.ui.pushButton_verkaufen.clicked.connect(self.verkaufenclick)

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen
    def kaufenclick(self):
        self.spieler.wertpapierKaufen(int(str(self.ui.spinBox_anzahlKaufen.value())), self.aktuellerticker)
    def verkaufenclick(self):
        self.spieler.wertpapierVerkaufen(int(str(self.ui.spinBox_anzahlVerkaufen.value())), self.aktuellerticker)
    def suche( self ):
        self.ui.listWidget_suchergebnis.clear()
        phrase = self.ui.plainTextEdit_aktiensuche.toPlainText()
        liste = ["%s (%s)" % (e[0], e[1]) for e in self.daten.tickers.inhaltSuchen(phrase)]
        self.ui.listWidget_suchergebnis.addItems(liste)

    def launchAktieninfo( self, qListItem ):
        label = qListItem.text()
        ticker = label.split('(')[1][:-1]
        self.aktuellerticker = ticker
        self.ui.tabWidget.setTabText(3, label)
        self.ui.tabWidget.setTabVisible(3, True)
        self.ui.tabWidget.setCurrentIndex(3)
        self.konfiguriereAktieninfo(ticker)


    def konfiguriereAktieninfo( self, ticker: str ):
        pass


if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()
