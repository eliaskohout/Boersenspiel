"""
SPIELER.py -> Ein Klasse, die Informationen und Methoden bezüglich des Spielers enthält.
"""


class SPIELER:

    def __init__(self, name, startguthaben: float = 0.0):  # Konstruktor
        self.name = name
        self.guthaben = startguthaben
