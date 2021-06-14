"""
SPIELER.py -> Ein Klasse, die Informationen und Methoden bezüglich des Spielers enthält.
"""
import time


class SPIELER:

    def __init__(self, name: str, preisfunc: 'funktion', startguthaben=0.0):  # Konstruktor
        self.tickerpreisErhalten = preisfunc

        self.name = name
        self.guthaben = 100000
        self.guthabenHistorie = []
        self.guthabenAendern(startguthaben)
        self.aktienliste = {}
        self.OrderGebuehren = 0

    def guthabenAendern(self, betrag: int):
        self.guthaben += betrag
        self.guthabenHistorie.append({
            'Datum': time.strftime("%d %m %y"),
            'Uhrzeit': time.strftime("%H %M %S"),
            'Guthaben': self.guthaben
        })

    def nameAendern(self, neuerName: str):
        self.name = neuerName

    def aktienAnzahlErhalten( self, ticker: str):
        if ticker not in self.aktienliste:
            return 0
        return self.aktienliste[ticker]

    def wertpapierKaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            self.aktienliste[wertpapier] = 0
        preis = self.tickerpreisErhalten(wertpapier)
        if anzahl * preis > self.guthaben:
            anzahl = int(self.guthaben / preis)
        self.guthabenAendern(anzahl * (-1) * preis-self.OrderGebuehren)
        self.aktienliste[wertpapier] += anzahl
        print("%s hat %d Wertpapiere (%s) zum Stückpreis von %d € gekauft." % (self.name, anzahl, wertpapier, preis))

    def wertpapierVerkaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            return
        preis = self.tickerpreisErhalten(wertpapier)
        anzahl = min(anzahl, self.aktienliste[wertpapier])
        self.guthabenAendern(anzahl * preis-self.OrderGebuehren)
        self.aktienliste[wertpapier] -= anzahl
        if self.aktienliste[wertpapier] == 0:
            self.aktienliste.pop(wertpapier)
        print("%s hat %d Wertpapiere (%s) zum Stückpreis von %d € verkauft." % (self.name, anzahl, wertpapier, preis))

    def depotwertBerechnen(self):
        depotwert = 0
        for i in self.aktienliste:
            depotwert += self.aktienliste[i] * self.tickerpreisErhalten(i)
        return depotwert
