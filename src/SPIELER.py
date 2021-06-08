"""
SPIELER.py -> Ein Klasse, die Informationen und Methoden bezüglich des Spielers enthält.
"""

import time
import src.DATEN as DATEN


class SPIELER:

    def __init__(self, name, startguthaben=0.0):  # Konstruktor
        self.name = name
        self.guthaben = 100000
        self.guthabenHistorie = []
        self.guthabenAendern(startguthaben)
        self.aktienliste = {}
        self.d = DATEN.DATEN()

    def guthabenAendern(self, betrag: int):
        self.guthaben += betrag
        self.guthabenHistorie.append({
            'Datum': time.strftime("%d %m %y"),
            'Uhrzeit': time.strftime("%H %M %S"),
            'Guthaben': self.guthaben
        })

    def nameAendern(self, neuerName: str):
        self.name = neuerName

    def wertpapierKaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            self.aktienliste[wertpapier] = 0
        preis = self.d.tickerpreisErhalten(wertpapier, von="heute")["Adj Close"][0]
        if anzahl * preis > self.guthaben:
            anzahl = int(self.guthaben / preis)
        self.guthabenAendern(anzahl * (-1) * preis)
        self.aktienliste[wertpapier] += anzahl
        print("gekauft")

    def wertpapierVerkaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            return
        preis = self.d.tickerpreisErhalten(wertpapier, von="heute")[0]
        anzahl = min(anzahl, self.aktienliste[wertpapier])
        self.guthabenAendern(anzahl * preis)

        self.aktienliste[wertpapier] -= anzahl
        self.aktienliste.pop(wertpapier, None)
        print("verkauft")

    def depotwertBerechnen(self):
        depotwert = 0
        for i in self.aktienliste:
            depotwert += self.aktienliste[i] * self.d.tickerpreisErhalten(i)[0]
        return depotwert

    def guthaben():
        return self.guthaben
