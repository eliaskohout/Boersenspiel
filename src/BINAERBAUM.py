"""
BINAERBAUM.py -> Klassen zum effeizienten Speicher und durchsuchen von Daten.
"""

import os.path
import json

class BINAERBAUM:
    """ Eine KLasse, die als 'Stativ' für den Baum dient, von hier wird der Baum organisiert.

    Attribute:
        - wurzel: Der Ursprung des Binärbaums
        - name: Name des Binärbaums, für das abspeichern wichtig
    Methoden:
        - __init__
        - sortiertEinfuegen
        - removeItem
        - inOrderAusgeben
        - bauBaumAusListe
        - gibBaumAusListe
        - inhaltSuchen
        - gibAnzahlElemente
        - balanceTree
        - saveToFile
        - buildFromFile

    """
    def __init__( self, name: str, sortiertNach: str ):
        self.wurzel = ABSCHLUSS()
        self.name = name
        self.sortiertNach = sortiertNach
        self.buildFromFile(name)

    def sortiertEinfuegen( self, inhalt: list ):
        """ Sortiertes einfügen eines Elements."""
        self.wurzel = self.wurzel.sortiertEinfuegen(inhalt, self.sortiertNach)

    def removeItem( self, inhalt ):
        liste = self.inOrderAusgeben().remove(inhalt)
        self.bauBaumAusListe(liste)

    def inOrderAusgeben( self ) -> list:
        """ Gibt alle Element des Baums als Liste in order aus."""
        return self.wurzel.inOrderAusgeben()

    def bauBaumAusListe( self, liste: list ):
        """ Baut einen Baum vollständig neu auf, hierfür wird eine Liste verwendet."""
        self.wurzel = self.gibBaumAusListe(liste)

    def gibBaumAusListe( self, liste: list ) -> 'KNOTEN':
        liste = sorted(liste, key=lambda k: k[self.sortiertNach])
        laengeListe = len(liste)
        if laengeListe == 0:
            return ABSCHLUSS()

        mitte = laengeListe//2  # Abrunden
        linkeListe  = liste[:mitte]
        rechteListe = liste[mitte +1:]
        return KNOTEN(liste[mitte], self.gibBaumAusListe(linkeListe), self.gibBaumAusListe(rechteListe))

    def inhaltSuchen( self, phrase: str, modus ='b' ) -> list:
        """ Durchsucht alle ersten Elemente des Inhalts nach Übereinstimmungen mit dem 'item'.

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
            return self.wurzel.sucheBeginn(phrase, self.sortiertNach)
        if modus == 'e':
            return self.wurzel.sucheExakt(phrase, self.sortiertNach)

    def gibAnzahlElemente( self ) -> int:
        return len(self.inOrderAusgeben())

    def balanceTree( self ):
        """ Sorgt dafür, dass der Baum ausgeglichen ist. """
        self.bauBaumAusListe(self.inOrderAusgeben())

    def saveToFile( self ):
        """Schreibt den Inhalt des Baums in eine Datei. Die Dateiendung (.binbaum) wird automatisch angefügt."""
        string = ""
        with open("./data/{}.binbaum".format(self.name), 'w+', encoding = "utf8") as file_obj:
            for dictionary in self.inOrderAusgeben():
                for key, val in dictionary.items():
                    string += "%s;%s;" % (key, val)
                file_obj.write(string + "\n")
                string = ""

    def buildFromFile( self, name =None ):
        """Baut den Baum aus einer Datei auf. Die Dateiendung (.binbaum) wird automatisch angefügt."""
        if name == None:
            name = self.name
        pfad = "./data/{}.binbaum".format(name)
        if os.path.exists(pfad):
            liste = []
            temp_dict = {}
            with open(pfad , 'r', encoding = "utf8") as file_obj:
                for zeile in file_obj:
                    spalten = zeile[:-1].split(';')
                    for ind, val in enumerate(spalten):
                        if ind%2 == 1:
                            temp_dict[spalten[ind-1]] = val
                    liste.append(temp_dict)
                    temp_dict = {}
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

    def sortiertEinfuegen( self, inhalt: list, key: str ):
        if self.inhalt[key] > inhalt[key]:
            self.links = self.links.sortiertEinfuegen(inhalt)
        elif self.inhalt[0] < inhalt[0]:
            self.rechts = self.rechts.sortiertEinfuegen(inhalt)
        else:
            self.inhalt = inhalt
        return self

    def inOrderAusgeben( self ):
        return self.links.inOrderAusgeben() + [self.inhalt] + self.rechts.inOrderAusgeben()

    def sucheExakt( self, phrase: str , key: str):
        if self.inhalt[key] > phrase:
            return self.links.sucheExakt(phrase, key)
        elif self.inhalt[key] < phrase:
            return self.rechts.sucheExakt(phrase, key)
        else:
            return self.inhalt

    def sucheBeginn(self, phrase: str, key: str):
        erg1 = self.links.sucheBeginn(phrase, key)
        erg2 = self.rechts.sucheBeginn(phrase, key)
        erg3 = []
        if self.inhalt[key][:len(phrase)].lower() == phrase.lower():
            erg3 = [self.inhalt]
        return erg1 + erg2 + erg3

class ABSCHLUSS():

    def __init__( self ):
        pass

    def sortiertEinfuegen( self, inhalt ):
        return KNOTEN(inhalt)

    def inOrderAusgeben( self ):
        return []

    def sucheExakt( self, phrase, key ):
        return []

    def sucheBeginn( self, phrase, key):
        return []
