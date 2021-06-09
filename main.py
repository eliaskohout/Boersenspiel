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

        self.aktuellerTicker = ""

        self.daten = D.DATEN()
        self.spieler = S.SPIELER('Bob', self.daten.aktuellenTickerpreisErhalten )

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabVisible(3, False)
        self.aktualisiereTabProtfolio()

        #self.daten.tickerErneuern()
        #self.daten.tickerbaum.saveToFile()

        # Hier können die Methoden mit den Signalen der Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)
        self.ui.listWidget_suchergebnis.itemDoubleClicked.connect(self.launchAktieninfo)
        self.ui.listWidget_gekaufteAktien.itemDoubleClicked.connect(self.launchAktieninfo)
        self.ui.pushButton_kaufen.clicked.connect(self.kaufenclick)
        self.ui.pushButton_kaufen.clicked.connect(self.aktualisiereAktienanzahlLabel)
        self.ui.pushButton_verkaufen.clicked.connect(self.verkaufenclick)
        self.ui.pushButton_verkaufen.clicked.connect(self.aktualisiereAktienanzahlLabel)
        self.ui.tabWidget.currentChanged.connect(self.aktualisiereTabProtfolio)
        self.ui.pushButton_preis.clicked.connect(self.aktualisierePreisLabel)

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen

    def kaufenclick( self ):
        self.spieler.wertpapierKaufen(int(str(self.ui.spinBox_anzahlKaufen.value())), self.aktuellerTicker)

    def verkaufenclick( self ):
        self.spieler.wertpapierVerkaufen(int(str(self.ui.spinBox_anzahlVerkaufen.value())), self.aktuellerTicker)

    def aktualisierePreisLabel( self ):
        tickerpreis = self.daten.aktuellenTickerpreisErhalten(self.aktuellerTicker)
        aktiensumme = self.ui.spinBox_anzahlKaufen.value() - self.ui.spinBox_anzahlVerkaufen.value()
        tickerpreis *= aktiensumme
        self.ui.label_preis.setText("%3.2f €" % tickerpreis)

    def aktualisiereAktienanzahlLabel( self ):
        self.ui.label_imBesitz.setText("Im Besitz: %d" % self.spieler.aktienAnzahlErhalten(self.aktuellerTicker))

    def suche( self ):
        self.ui.listWidget_suchergebnis.clear()
        phrase = self.ui.plainTextEdit_aktiensuche.toPlainText()
        liste = ["%s (%s)" % (e['name'], e['symbol']) for e in self.daten.tickerbaum.inhaltSuchen(phrase)]
        self.ui.listWidget_suchergebnis.addItems(liste)

    def launchAktieninfo( self, qListItem ):
        label = qListItem.text()
        ticker = label.split('(')[1][:-1]
        self.aktuellerTicker = ticker
        self.ui.tabWidget.setTabText(3, label)
        self.ui.tabWidget.setTabVisible(3, True)
        self.ui.tabWidget.setCurrentIndex(3)
        self.konfiguriereAktieninfo(ticker)

    def konfiguriereAktieninfo( self, ticker: str ):
        self.ui.label_preis.setText("   €")

    def aktualisiereTabProtfolio( self , i =0 ):
        if i != 0: return
        self.ui.listWidget_gekaufteAktien.clear()
        itemlist = ["%s (%s)" % (self.daten.aktiennameErhalten(e), e) for e in self.spieler.aktienliste]
        self.ui.listWidget_gekaufteAktien.addItems(itemlist)
        self.ui.label_depotwert.setText("Depotwert: %3.2f €" % self.spieler.depotwertBerechnen())
        self.ui.label_guthaben.setText( "Guthaben:  %3.2f €" % self.spieler.guthaben)


if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()
