"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.DATEN as D

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import threading


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
        self.aktualisiereTabPortfolio()

        #self.daten.tickerErneuern()
        #self.daten.tickerbaum.saveToFile()

        # Hier können die Methoden mit den Signalen der Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)
        self.ui.listWidget_suchergebnis.itemDoubleClicked.connect(self.launchAktieninfo)
        self.ui.listWidget_gekaufteAktien.itemDoubleClicked.connect(self.launchAktieninfo)
        self.ui.pushButton_kaufen.clicked.connect(self.kaufenclick)
        self.ui.pushButton_kaufen.clicked.connect(self.aktualisiereImBesitzLabel)
        self.ui.pushButton_verkaufen.clicked.connect(self.verkaufenclick)
        self.ui.pushButton_verkaufen.clicked.connect(self.aktualisiereImBesitzLabel)
        self.ui.tabWidget.currentChanged.connect(self.aktualisiereTabPortfolio)
        self.ui.pushButton_preis.clicked.connect(self.aktualisierePreisLabel)
        self.ui.pushButton_Gebuehr.clicked.connect(self.aktualisierenOrderGebuehren)
        self.ui.pushButton_DepotGuthaben.clicked.connect(self.aktualisierenDepotguthaben)
        self.ui.pushButton_save.clicked.connect(self.spieler.safe)
        self.ui.pushButton_load.clicked.connect(self.spieler.load)
    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen

    def kaufenclick( self, threaded=True):
        if threaded:
            self.imHintergrundAusfuehren( self.kaufenclick, (False) )
            return
        self.spieler.wertpapierKaufen(int(self.ui.spinBox_anzahlKaufen.value()), self.aktuellerTicker)
        self.aktualisiereImBesitzLabel(threaded=False)
        curserZuruecksetzen()

    def verkaufenclick( self, threaded=True):
        if threaded:
            self.imHintergrundAusfuehren( self.kaufenclick, (False) )
            return
        self.spieler.wertpapierVerkaufen(int(self.ui.spinBox_anzahlVerkaufen.value()), self.aktuellerTicker)
        self.aktualisiereImBesitzLabel(threaded=False)
        curserZuruecksetzen()

    def aktualisierePreisLabel( self, threaded=True):
        if threaded:
            self.imHintergrundAusfuehren( self.aktualisierePreisLabel, (False))
            return
        tickerpreis = self.daten.aktuellenTickerpreisErhalten(self.aktuellerTicker)
        aktiensumme = self.ui.spinBox_anzahlKaufen.value() - self.ui.spinBox_anzahlVerkaufen.value()
        tickerpreis *= aktiensumme
        self.ui.label_preis.setText("%3.2f €" % tickerpreis)
        curserZuruecksetzen()

    def aktualisiereImBesitzLabel( self, threaded=True):
        if threaded:
            self.imHintergrundAusfuehren( self.aktualisiereImBesitzLabel, (False))
            return
        self.ui.label_imBesitz.setText("Im Besitz: %d" % self.spieler.aktienAnzahlErhalten(self.aktuellerTicker))
        curserZuruecksetzen()

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

    def aktualisiereTabPortfolio( self , i =0, threaded=True ):
        if i != 0: return
        if threaded:
            self.imHintergrundAusfuehren( self.aktualisiereTabPortfolio, (i, False) )
            return
        self.ui.listWidget_gekaufteAktien.clear()
        itemlist = ["%s (%s)" % (self.daten.aktiennameErhalten(e), e) for e in self.spieler.aktienliste]
        self.ui.listWidget_gekaufteAktien.addItems(itemlist)
        self.ui.label_depotwert.setText("Depotwert: %3.2f €" % self.spieler.depotwertBerechnen())
        self.ui.label_guthaben.setText( "Guthaben:  %3.2f €" % self.spieler.guthaben)
        curserZuruecksetzen()

    def imHintergrundAusfuehren( self, funktion: 'funktion', arguments: tuple):
        curserAufBeschaeftigt()
        x = threading.Thread(target=funktion, args=arguments)
        x.start()

    def aktualisierenOrderGebuehren(self):
        self.spieler.OrderGebuehren = self.ui.OrderGebuehr.value()

    def aktualisierenDepotguthaben(self):
        self.spieler.guthaben = self.ui.SpinBox_Depotguthaben.value()

def curserAufBeschaeftigt():
    app.setOverrideCursor(qtc.Qt.BusyCursor)

def curserZuruecksetzen():
    app.restoreOverrideCursor()

if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()

