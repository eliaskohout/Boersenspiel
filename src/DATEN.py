"""
DATEN.py -> Die Klasse DATEN und MARKETSTACK, die den Zugriff auf die marketstack.com API koordiniert und damit auch das Erhalten und
Aufbereiten von Aktiendaten.
"""
import src.BINAERBAUM as b

import requests
import platform
import subprocess
import pandas_datareader as web
from datetime import date


class DATEN:
    """ Eine Klasse, die das Sammeln, Ordnen und Speichern der Daten organisiert

    Attribute:
        - api: Instanz der Klasse MARKETSTACK
        - tickers: Instanz der Klasse BINAERBAUM, speichert alle verfügbaren Ticker
    Methoden:
        - __init__
        - tickerErneuern
    """
    def __init__( self ):
        self.api = MARKETSTACK()
        self.tickers = b.BINAERBAUM('tickers')
        self.aktiendatenCache = {}

    def tickerErneuern( self ):
        liste = self.api.getTickerListe()
        self.tickers.bauBaumAusListe(liste)

    def tickerpreisErhalten( self, ticker: str, von="1980-12-12", bis="heute"):
        #TODO Sichern im Cache
        if bis == "heute":
            bis = date.today()
        if von == "heute":
            von = date.today()
        daten = web.DataReader(ticker, "yahoo", start=von, end=bis)
        return daten

class MARKETSTACK:
    """ Eine Klasse, die den Zugriff auf die Marketstack-API regelt.

    Attribute:
        - API_key:   Notwendig um auf die API zugreifen zu können
        - online:    Für den Netzwerksstatus

    Methoden:
        - __init__
        - ping
        - netzwerktest
        - getEOD
        - getEODbyDate
        - getTickerListe
    """

    def __init__(self):  # Konstruktor
        self.API_Key = "f644767528a615d6757c5658e5d9ef7e"
        self.online = None

        self.netzwerktest()

    def ping(self, host='google.com') -> bool:
        """ Zum pingen einer Domain, unabhängig von der Platform

        Input:
            host: Ein String einer Domain, die gepingt werden soll
        Output:
            True,  falls die Domain erreichbar ist
            False, sonst
        """
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', host]
            return subprocess.call(command) == 0
        except FileNotFoundError:
            print("FileNotFoundError: 'ping' konnte nicht ausgeführt werden.")
            return False

    def netzwerktest(self) -> None:
        """Testet ob 'marketstack.com' erreichbar ist und gibt das Ergebnis auf der Konsole aus
        """
        print("Teste Netzwerk...")
        self.online = self.ping("marketstack.com")
        if self.online:
            print('marketstack.com API bereit.')
        else:
            print("Error: Es konnte keine Verbindung zum marketstack.com aufgebaut werden.")

    def getEOD(self, ticker: str, limit =100, offset =0) -> dict:
        """ Zur Abfrage der End-of-Day Daten

        Input:
            ticker:  Der Ticker einer bestimmten Aktie, Übergabe mehrerer (max. 100) durch ein Komma getrennter Ticker möglich
            limit:   Definiert die Anzahl an Tagen bzw. Einträgen (max. 1000)
            offset:  Definiert eine Verschiebung des ersten Abgefragten Tages in Tagen
        Output:
            Ein dict mit den passenden Daten
        """
        parameter = {
            'access_key': self.API_Key,
            'symbols': ticker,
            'limit': limit,
            'offset': offset
        }
        api_ergebnis = requests.get('http://api.marketstack.com/v1/eod', parameter)  # HTTP GET Request
        return api_ergebnis.json()

    def getEODbyDate(self, ticker: str, date_from: str, date_to: str) -> dict:
        """ Zur Abfrage der End-of-Day Daten

        Input.
            ticker:     Der Ticker einer bestimmten Aktie, Übergabe mehrerer (max. 100) durch ein Komma getrennter Ticker möglich
            date_from: "Von"-Datum: "YYYY-MM-DD" oder im ISO-8601 Datum Format (bis zu 30 Jahre)
            date_to:   "Bis"-Datum: "YYYY-MM-DD" oder im ISO-8601 Datum Format
        Output:
            Ein dict mit den passenden Daten
        """
        parameter = {
            'access_key': self.API_Key,
            'symbols': ticker,
            'date_from': date_from,
            'date_to': date_to
        }
        api_ergebnis = requests.get('http://api.marketstack.com/v1/eod', parameter)  # HTTP GET Request
        return api_ergebnis.json()

    def getTickerListe(self) -> list:
        """Gibt eine Liste an abrufbaren (durch u.a. self.getEOD) Tickern bzw. Aktien aus.
        !! Nicht zu oft verwenden, verbraucht ca. 150 API-Abfragen !!

        Input:
            None
        Output:
            Lisete an Tuple -> [(Name, Ticker), (Name2, Ticker2), ...]

        """

        parameter = {
            'access_key':self.API_Key,
            'limit': 1000,
            'offset': 0
        }

        api_ergebnis = requests.get('http://api.marketstack.com/v1/tickers', parameter)  # HTTP GET Request
        api_ergebnis = api_ergebnis.json()

        total = api_ergebnis['pagination']['total']  # Erhalten der verfügbaren Ergebnisse
        rueckgabe = []

        for i in range( (-(-total//1000)) ):  # für den Aufgerundeten Wert
            api_ergebnis = requests.get('http://api.marketstack.com/v1/tickers', parameter)  # HTTP GET Request
            api_ergebnis = api_ergebnis.json()
            parameter['offset'] += 1000

            for j in api_ergebnis['data']:
                if ( j['has_eod'] == True ) and ( j['name'] != None and j['name'] != '' ) :
                    rueckgabe.append( (j['name'], j['symbol']) )

        return rueckgabe
