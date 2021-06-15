"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.DATEN as D

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QPixmap
import threading, sys


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aktuellerTicker = ""
        self.waehrung = "€"

        name, nichtCancel = self.abfrageName()
        if not nichtCancel and name == "":
            sys.exit()
        
        self.daten = D.DATEN()
        self.spieler = S.SPIELER(name, self.daten.aktuellenTickerpreisErhalten )

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabVisible(3, False)
        self.aktualisiereTabPortfolio()

        #self.daten.tickerErneuern()
        #self.daten.tickerbaum.saveToFile()

        # Hier können die Methoden mit den Signalen der Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)
        self.ui.listWidget_suchergebnis.itemDoubleClicked.connect(lambda listitem: self.bg(self.launchAktieninfo, (listitem, True)))
        self.ui.listWidget_gekaufteAktien.itemDoubleClicked.connect(lambda listitem: self.bg(self.launchAktieninfo, (listitem, True)))
        self.ui.pushButton_kaufen.clicked.connect(lambda: self.bg(self.kaufenclick, (True)))
        self.ui.pushButton_kaufen.clicked.connect(lambda: self.bg(self.aktualisiereImBesitzLabel, (True)))
        self.ui.pushButton_verkaufen.clicked.connect(lambda: self.bg(self.verkaufenclick, (True)))
        self.ui.pushButton_verkaufen.clicked.connect(lambda: self.bg(self.aktualisiereImBesitzLabel, (True)))
        self.ui.tabWidget.currentChanged.connect(self.aktualisiereTabPortfolio)
        self.ui.pushButton_preis.clicked.connect(lambda: self.bg(self.aktualisierePreisLabel, (True)))
        self.ui.pushButton_refresh_Gebuehr.clicked.connect(lambda x: self.bg(self.aktualisierenOrderGebuehren, (x, True)))
        self.ui.pushButton_refresh_DepotGuthaben.clicked.connect(self.aktualisierenDepotguthaben)
        self.ui.pushButton_save.clicked.connect(self.spieler.safe)
        self.ui.pushButton_load.clicked.connect(self.spieler.load)
        self.ui.pushButton_refresh_waehrung.clicked.connect(self.aktualisiereWaehrung)

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen
    def abfrageName( self ):
        output = qtw.QInputDialog.getText(self, "Namenswahl", "Dein Name:", qtw.QLineEdit.Normal, "")
        return output

    def kaufenclick( self, threaded=False ):
        self.spieler.wertpapierKaufen(int(self.ui.spinBox_anzahlKaufen.value()), self.aktuellerTicker)
        self.aktualisiereImBesitzLabel(threaded=False)
        if threaded: cursorZuruecksetzen()

    def verkaufenclick( self, threaded=False ):
        self.spieler.wertpapierVerkaufen(int(self.ui.spinBox_anzahlVerkaufen.value()), self.aktuellerTicker)
        self.aktualisiereImBesitzLabel(threaded=False)
        if threaded: cursorZuruecksetzen()

    def aktualisierePreisLabel( self, threaded=False ):
        tickerpreis = self.daten.aktuellenTickerpreisErhalten(self.aktuellerTicker)
        aktiensumme = self.ui.spinBox_anzahlKaufen.value() - self.ui.spinBox_anzahlVerkaufen.value()
        tickerpreis *= aktiensumme
        self.ui.label_preis.setText("%3.2f %s" % (tickerpreis, self.waehrung))
        if threaded: cursorZuruecksetzen()

    def aktualisiereImBesitzLabel( self, threaded=False ):
        self.ui.label_imBesitz.setText("Im Besitz: %d" % self.spieler.aktienAnzahlErhalten(self.aktuellerTicker))
        if threaded: cursorZuruecksetzen()

    def suche( self ):
        self.ui.listWidget_suchergebnis.clear()
        phrase = self.ui.plainTextEdit_aktiensuche.toPlainText()
        liste = ["%s (%s)" % (e['name'], e['symbol']) for e in self.daten.tickerbaum.inhaltSuchen(phrase)]
        self.ui.listWidget_suchergebnis.addItems(liste)

    def launchAktieninfo( self, qListItem, threaded=False ):
        label = qListItem.text()
        ticker = label.split('(')[1][:-1]
        self.aktuellerTicker = ticker
        self.ui.tabWidget.setTabText(3, label)
        self.ui.tabWidget.setTabVisible(3, True)
        self.ui.tabWidget.setCurrentIndex(3)
        self.konfiguriereAktieninfo(ticker)
        if threaded: cursorZuruecksetzen()

    def konfiguriereAktieninfo( self, ticker: str ):
        self.ui.label_preis.setText(self.waehrung)
        self.aktualisiereImBesitzLabel(threaded=False)
        self.daten.tickerpreisErhaltenInTagen(ticker, 7).plot().get_figure().savefig("data/charts/chart.jpeg")
        self.ui.label_chart_1Woche.setPixmap(QPixmap("data/charts/chart.jpeg"))
        self.daten.tickerpreisErhaltenInTagen(ticker, 30).plot().get_figure().savefig("data/charts/chart.jpeg")
        self.ui.label_chart_1Monat.setPixmap(QPixmap("data/charts/chart.jpeg"))
        self.daten.tickerpreisErhaltenInTagen(ticker, 180).plot().get_figure().savefig("data/charts/chart.jpeg")
        self.ui.label_chart_6Monate.setPixmap(QPixmap("data/charts/chart.jpeg"))
        self.daten.tickerpreisErhaltenInTagen(ticker, 365).plot().get_figure().savefig("data/charts/chart.jpeg")
        self.ui.label_chart_1Jahr.setPixmap(QPixmap("data/charts/chart.jpeg"))


    def aktualisiereTabPortfolio( self , i =0, threaded=False ):
        if i != 0: return
        self.ui.label_begruessung.setText("Hallo, %s!" % self.spieler.name)

        self.ui.listWidget_gekaufteAktien.clear()
        itemlist = ["%s (%s)" % (self.daten.aktiennameErhalten(e), e) for e in self.spieler.aktienliste]
        self.ui.listWidget_gekaufteAktien.addItems(itemlist)
        self.ui.listWidget_historie.clear()
        itemlist = ["%sx %s zum Einzelpreis von %3.2f %s" % (e['Volumen'], e['Ticker'], e['Preis'], self.waehrung) for e in self.spieler.kaufHistorie]
        itemlist.reverse()
        self.ui.listWidget_historie.addItems(itemlist)

        self.ui.label_depotwert.setText("Depotwert: %3.2f %s" % (self.spieler.depotwertBerechnen(), self.waehrung))
        self.ui.label_guthaben.setText( "Guthaben:  %3.2f %s" % (self.spieler.guthaben, self.waehrung))
        if threaded: cursorZuruecksetzen()

    def bg( self, funktion: 'funktion', arguments: tuple):  # im Hintergrund ausfuehren
        cursorAufBeschaeftigt()
        x = threading.Thread(target=funktion, args=arguments)
        x.start()

    def aktualisierenOrderGebuehren( self ):
        self.spieler.OrderGebuehren = self.ui.spinBox_OrderGebuehr.value()

    def aktualisierenDepotguthaben( self ):
        self.spieler.guthaben = self.ui.spinBox_Depotguthaben.value()

    def aktualisiereWaehrung( self ):
        self.waehrung = self.ui.plainTextEdit_Waehrung.toPlainText()


def main():
    pass

def cursorAufBeschaeftigt():
    app.setOverrideCursor(qtc.Qt.BusyCursor)

def cursorZuruecksetzen():
    app.restoreOverrideCursor()

if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()

