"""
SPIELER.py -> Ein Klasse, die Informationen und Methoden bezüglich des Spielers enthält.
"""

import time


class SPIELER:

    def __init__(self, name, startguthaben = 0.0):  # Konstruktor
        self.name = name
        self.guthaben = 0
        self.guthabenHistorie = []
        self.guthabenAendern(startguthaben)

    def guthabenAendern (self, betrag: int):
        self.guthaben += betrag
        self.guthabenHistorie.append({
            'Datum': time.strftime("%d %m %y"),
            'Uhrzeit': time.strftime("%H %M %S"),
            'Guthaben': self.guthaben
        })

    def nameAendern (self, neuerName: str):
        self.name = neuerName

    
