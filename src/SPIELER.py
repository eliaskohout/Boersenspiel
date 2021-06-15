"""
SPIELER.py -> Ein Klasse, die Informationen und Methoden bezüglich des Spielers enthält.
"""
import time, json, os


class SPIELER:

    def __init__(self, name: str, preisfunc: 'funktion', startguthaben=1000.0):  # Konstruktor
        self.tickerpreisErhalten = preisfunc
        self.name = name
        self.startguthaben = startguthaben
        self.guthaben = startguthaben
        self.kaufHistorie = []
        self.aktienliste = {}
        self.OrderGebuehren = 0
        self.waehrung = "€"
        if os.path.exists("daten/spielstand_%s.json" % name):
            self.profil_laden(name)
        else:
            self.profil_sichern()

    def nameAendern(self, neuerName: str):
        self.name = neuerName

    def aktienAnzahlErhalten(self, ticker: str):
        if ticker not in self.aktienliste:
            return 0
        return self.aktienliste[ticker]

    def wertpapierKaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            self.aktienliste[wertpapier] = 0
        preis = self.tickerpreisErhalten(wertpapier)
        if anzahl * preis > self.guthaben:
            anzahl = int(self.guthaben / preis)
        self.guthaben += anzahl * (-1) * preis - self.OrderGebuehren
        self.aktienliste[wertpapier] += anzahl

        self.kaufHistorie.append({
            'Datum': time.strftime("%d %m %y"),
            'Uhrzeit': time.strftime("%H %M %S"),
            'Ticker':  wertpapier,
            'Volumen': anzahl,
            'Preis': preis
        })
        print("%s hat %d Wertpapiere (%s) zum Stückpreis von %d € gekauft." % (self.name, anzahl, wertpapier, preis))

    def wertpapierVerkaufen(self, anzahl: int, wertpapier: str):
        if wertpapier not in self.aktienliste:
            return
        preis = self.tickerpreisErhalten(wertpapier)
        anzahl = min(anzahl, self.aktienliste[wertpapier])
        self.guthaben += anzahl * preis - self.OrderGebuehren
        self.aktienliste[wertpapier] -= anzahl
        if self.aktienliste[wertpapier] == 0:
            self.aktienliste.pop(wertpapier)

        self.kaufHistorie.append({
            'Datum': time.strftime("%d %m %y"),
            'Uhrzeit': time.strftime("%H %M %S"),
            'Ticker':  wertpapier,
            'Volumen': -1*anzahl,
            'Preis': preis
        })
        print("%s hat %d Wertpapiere (%s) zum Stückpreis von %d € verkauft." % (self.name, anzahl, wertpapier, preis))

    def depotwertBerechnen(self):
        depotwert = 0
        for i in self.aktienliste:
            depotwert += self.aktienliste[i] * self.tickerpreisErhalten(i)
        return depotwert

    def profile_auflisten(self) -> list:
        return [e[:-5] for e in os.listdir('./data/profile/')]

    def profil_sichern(self):
        dict_ = {}
        dict_['aktienliste'] = self.aktienliste
        dict_['guthaben'] = self.guthaben
        dict_['kaufhistorie'] = self.kaufHistorie
        dict_['ordergebueren'] = self.OrderGebuehren
        dict_['waehrung'] = self.waehrung
        with open("data/profile/%s.json" % self.name, "w") as outfile:
            json.dump(dict_, outfile)

    def profil_laden(self, name):
        if not os.path.exists("data/profile/%s.json" % name):
            return
        with open("data/profile/%s.json" % self.name, "r") as infile:
            dict_ = json.load(infile)
        self.guthaben = dict_['guthaben']
        self.aktienliste = dict_['aktienliste']
        self.kaufHistorie = dict_['kaufhistorie']
        self.OrderGebuehren = dict_['ordergebueren']
        self.waehrung = dict_['waehrung']
        self.name = name

    def profil_neu(self, name: str):
        self.profil_sichern()
        self.name = name
        self.guthaben = self.startguthaben
        self.aktienliste = {}
        self.kaufHistorie = []
        self.OrderGebuehren = 0
        self.waehrung = '€'
        self.profil_sichern()

    def profil_loeschen(self, name):
        os.remove("data/profile/%s.json" % name)
