"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.DATEN as D

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import threading, sys, os


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aktuellerTicker = ""
        if os.listdir('./data/profile') == []:
            name, nichtCancel = self.abfrageName()
            if not nichtCancel and name == "":
                sys.exit()
        else:
            name = os.listdir('./data/profile')[0][:-5]
        
        self.daten = D.DATEN()
        self.spieler = S.SPIELER(name, self.daten.aktuellenTickerpreisErhalten )

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabVisible(3, False)
        self.aktualisiereTabPortfolio()
        self.ui.plotWidget.setBackground('w')
        self.ui.plotWidget.setAntialiasing(True)


        # Hier können die Methoden mit den Signalen der Widgets verbunden werden

        self.ui.pushButton_aktiensuche.clicked.connect(self.suche)
        self.ui.listWidget_suchergebnis.itemDoubleClicked.connect(lambda listitem: self.bg(self.launchAktieninfo, (listitem, True,)))
        self.ui.listWidget_gekaufteAktien.itemDoubleClicked.connect(lambda listitem: self.bg(self.launchAktieninfo, (listitem, True,)))
        self.ui.pushButton_kaufen.clicked.connect(lambda: self.bg(self.kaufenclick, (True,)))
        self.ui.pushButton_verkaufen.clicked.connect(lambda: self.bg(self.verkaufenclick, (True,)))
        self.ui.tabWidget.currentChanged.connect(lambda x: self.bg(self.aktualisiereTabPortfolio, (x, True,)))
        self.ui.tabWidget.currentChanged.connect(self.aktualisiereTabEinstellungen)
        self.ui.pushButton_preis.clicked.connect(lambda: self.bg(self.aktualisierePreisLabel, (True,)))
        self.ui.pushButton_refresh_Gebuehr.clicked.connect(self.aktualisierenOrderGebuehren)
        self.ui.pushButton_refresh_DepotGuthaben.clicked.connect(self.aktualisierenDepotguthaben)
        self.ui.pushButton_profil_loeschen.clicked.connect(self.profilLoeschen)
        self.ui.pushButton_profil_laden.clicked.connect(self.profilLaden)
        self.ui.pushButton_neues_profil.clicked.connect(self.profilErstellen)
        self.ui.pushButton_refresh_waehrung.clicked.connect(self.aktualisiereWaehrung)
        self.ui.pushButton_ticker_aktualisieren.clicked.connect(lambda: self.bg(self.tickerAktualisieren, (True,)))

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen
    def abfrageName( self ):
        output = qtw.QInputDialog.getText(self, "Namenswahl", "Dein Name:", qtw.QLineEdit.Normal, "")
        return output

    def profilErstellen( self ):
        name, nichtCancel = self.abfrageName()
        if nichtCancel and name != '':
            self.spieler.profil_neu(name)
            self.aktualisiereTabEinstellungen()
        
    def profilLoeschen( self ):
        current = self.ui.listWidget_profile.currentItem()
        if current.text() != self.spieler.name:
            self.spieler.profil_loeschen(current.text())
            self.ui.listWidget_profile.removeItemWidget(current)
            self.aktualisiereTabEinstellungen()
    
    def profilLaden( self ):
        name = self.ui.listWidget_profile.currentItem().text()
        self.spieler.profil_laden(name)
        self.aktualisiereTabEinstellungen()
    
    def aktualisiereTabEinstellungen( self, i=2 ):
        if i != 2: return
        self.ui.listWidget_profile.clear()
        self.ui.listWidget_profile.addItems(self.spieler.profile_auflisten())
        self.ui.spinBox_OrderGebuehr.setValue(self.spieler.OrderGebuehren)
        self.ui.groupBox_profile.setTitle("Profile (zurzeit %s)" % self.spieler.name)

    def tickerAktualisieren( self, threaded=False):
        self.daten.tickerErneuern()
        self.daten.tickerbaum.saveToFile()
        if threaded: cursorZuruecksetzen()

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
        self.ui.label_preis.setText("%3.2f %s" % (tickerpreis, self.spieler.waehrung))
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
        self.ui.label_preis.setText(self.spieler.waehrung)
        self.aktualisiereImBesitzLabel(threaded=False)
        self.ui.plotWidget.plot(self.daten.tickerpreisErhalten(ticker), pen='b', clear=True)
        #self.ui.plotWidget.plot(self.daten.tickerpreisErhalten(ticker, key='Volume'), pen='g')

    def aktualisiereTabPortfolio( self , i =0, threaded=False ):
        if i != 0:
            if threaded: cursorZuruecksetzen()
            return
        self.ui.label_begruessung.setText("Hallo, %s!" % self.spieler.name)

        self.ui.listWidget_gekaufteAktien.clear()
        itemlist = ["%s (%s)" % (self.daten.aktiennameErhalten(e), e) for e in self.spieler.aktienliste]
        self.ui.listWidget_gekaufteAktien.addItems(itemlist)
        self.ui.listWidget_historie.clear()
        itemlist = ["%sx %s zum Einzelpreis von %3.2f %s" % (e['Volumen'], e['Ticker'], e['Preis'], self.spieler.waehrung) for e in self.spieler.kaufHistorie]
        itemlist.reverse()
        self.ui.listWidget_historie.addItems(itemlist)

        self.ui.label_depotwert.setText("Depotwert: %3.2f %s" % (self.spieler.depotwertBerechnen(), self.spieler.waehrung))
        self.ui.label_guthaben.setText( "Guthaben:  %3.2f %s" % (self.spieler.guthaben, self.spieler.waehrung))
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
        self.spieler.waehrung = self.ui.plainTextEdit_Waehrung.toPlainText()
        self.ui.label_waehrung_depotguthaben_aendern.setText(self.spieler.waehrung)
        self.ui.label_waehrung_ordergebuehren.setText(self.spieler.waehrung)


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

