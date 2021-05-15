"""
BINAERBAUM.py -> Klassen zum effeizienten Speicher und durchsuchen von Daten.
"""

import os.path

class BINAERBAUM:
    """ Eine KLasse, die als 'Stativ' für den Baum dient, von hier wird der Baum organisiert.

    Attribute:
        -
    Methoden:
        -

    """
    def __init__( self, name ):
        self.wurzel = ABSCHLUSS()
        self.name = name
        self.buildFromFile(name)

    def sortiertEinfuegen( self, inhalt: list ):
        """ Sortiertes einfügen eines Elements."""
        self.wurzel = self.wurzel.sortiertEinfuegen(inhalt)

    def removeItem( self, inhalt ):
        pass

    def inOrderAusgeben( self ) -> list:
        """ Gibt alle Element des Baums als Liste in order aus."""
        return self.wurzel.inOrderAusgeben()

    def bauBaumAusListe( self, liste: list ):
        """ Baut einen Baum vollständig neu auf, hierfür wird eine Liste verwendet."""
        self.wurzel = self.gibBaumAusListe(liste)

    def gibBaumAusListe( self, liste: list ) -> 'KNOTEN':
        liste = sorted(liste)
        laengeListe = len(liste)
        if laengeListe == 0:
            return ABSCHLUSS()

        mitte = laengeListe//2  # Abrunden
        linkeListe  = liste[:mitte]
        rechteListe = liste[mitte +1:]
        return KNOTEN(liste[mitte], self.gibBaumAusListe(linkeListe), self.gibBaumAusListe(rechteListe))

    def inhaltSuchen( self, phrase: str, modus ='b' ) -> list:
        """ Durchsucht alle ersten Elemente des Inhalts nach übereinstimmungen mit dem 'item'.

        Input:
            - item: Muss ein String sein
            - mode: Bestimmt, wie nach Elemeneten gesucht werden soll
                    [e: exakte Übereinstimmung mit dem ersten Element des Datenarray
                     b: Übereinstimmung mit dem Beginn des ersten Elements des Datenarray, caseinsensitive]
        Output:
            Eine Liste mit dem Inhalt der Element, die zur Suchphrase passen,
            wenn nur Leerzeichen oder ein leerer String übergeben wird, wird der gesamte Baum 'in order' zurückgegeben
            wenn kein Eintrag gefunden wurde, wird eine leere Liste zurückgegeben
        """
        if phrase.strip() == '':
            return self.inOrderAusgeben()
        if modus == 'b':
            return self.wurzel.sucheBeginn(phrase)
        if modus == 'e':
            return self.wurzel.sucheExakt(phrase)

    def gibAnzahlElemente() -> int:
        return len(self.inOrderAusgeben())

    def balanceTree( self ):
        """ Sorgt dafür, dass der Baum ausgeglichen ist. """
        pass

    def saveToFile( self ):
        """Schreibt den Inhalt des Baums in eine Datei. Die Dateiendung (.binbaum) wird automatisch angefügt."""
        with open("./data/{}.binbaum".format(self.name), 'w+') as file_obj:
            for i in self.inOrderAusgeben():
                zeile = ''
                for j in i:
                    zeile += j + ";"
                zeile[:-1] += '\n'
                file_obj.write(zeile)

    def buildFromFile( self, name =None ):
        """Baut den Baum aus einer Datei auf. Die Dateiendung (.binbaum) wird automatisch angefügt."""
        if name == None:
            name = self.name
        pfad = "./data/{}.binbaum".format(name)
        if os.path.exists(pfad):
            liste = []
            with open(pfad , 'r') as file_obj:
                for zeile_string in file_obj:
                    elemente = zeile_string.strip().split(';')
                    liste += [elemente]
            self.bauBaumAusListe(liste)

class KNOTEN:
    """ Eine Klasse, die die Knoten des Binärbaums darstellt.

    Attribute:
        - inhalt: Der zu speichernde Inhalt
        - rechts: Nächster Knoten rechts
        - links: Nächster Knoten rechts
    Methoden:
        - __init__
        - sortiertEinfuegen
        - inOrderAusgeben
        - sucheExakt
        - sucheBeginn
    """
    def __init__( self, inhalt, rechts =None, links =None):
        self.inhalt = inhalt
        if rechts is None:
            self.rechts = ABSCHLUSS()
        else:
            self.rechts = rechts
        if links is None:
            self.links = ABSCHLUSS()
        else:
            self.links = links

    def sortiertEinfuegen( self, inhalt: list ):
        if self.inhalt[0] > inhalt[0]:
            self.links = self.links.sortiertEinfuegen(inhalt)
        elif self.inhalt[0] < inhalt[0]:
            self.rechts = self.rechts.sortiertEinfuegen(inhalt)
        else:
            self.inhalt = inhalt
        return self

    def inOrderAusgeben( self ):
        return self.links.inOrderAusgeben() + [self.inhalt] + self.rechts.inOrderAusgeben()

    def sucheExakt( self, phrase ):
        if self.inhalt[0] > phrase:
            return self.links.sucheExakt(phrase)
        elif self.inhalt[0] < phrase:
            return self.rechts.sucheExakt(phrase)
        else:
            return self.inhalt

    def sucheBeginn(self, phrase):
        erg1 = self.links.sucheBeginn(phrase)
        erg2 = self.rechts.sucheBeginn(phrase)
        erg3 = []
        if self.inhalt[0][:len(phrase)].lower() == phrase.lower():
            erg3 = [self.inhalt]
        return erg1 + erg2 + erg3

class ABSCHLUSS():

    def __init__( self ):
        pass

    def sortiertEinfuegen( self, inhalt ):
        return KNOTEN(inhalt)

    def inOrderAusgeben( self ):
        return []

    def sucheExakt( self, phrase ):
        return []

    def sucheBeginn( self, phrase ):
        return []
