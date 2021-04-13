"""
MARKETSTACK.py -> Ein Klasse, die den Zugriff auf die marketstack.com API koordiniert und damit auch das Erhalten und
Aufbereiten von Aktiendaten.
"""

import requests
import platform
import subprocess


class MARKETSTACK:

    def __init__(self):  # Konstruktor
        self.API_Key = "f644767528a615d6757c5658e5d9ef7e"
        self.online = None

        self.netzwerktest()

    def ping(self, host: str) -> bool:  # Ping eine Domain oder IP-Adresse
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', host]
            return subprocess.call(command) == 0
        except FileNotFoundError:
            print("FileNotFoundError: 'ping' konnte nicht ausgeführt werden.")
            return False

    def netzwerktest(self) -> None:
        print("Teste Netzwerk...")
        self.online = self.ping("marketstack.com")
        if self.online:
            print('marketstack.com API bereit.')
        else:
            print("Error: Es konnte keine Verbindung zum marketstack.com aufgebaut werden.")

    def getEOD(self, ticker: str, limit: int =100, offset: int =0) -> dict:  # Abfrage der End-of-Day Daten
        parameter = {
            'access_key': self.API_Key,
            'symbols': ticker,              # Der Ticker einer bestimmten Aktie
            'limit': limit,                 # Definiert die Anzahl an Tagen bzw. Einträgen (max. 1000)
            'offset': offset                # Definiert eine Verschiebung des ersten Abgefragten Tages in Tagen
        }
        api_ergebnis = requests.get('http://api.marketstack.com/v1/eod', parameter)  # HTTP GET Request
        return api_ergebnis.json()

    def getEODbyDate(self, ticker: str, date_from: str, date_to: str) -> dict:  # Abfrage der End-of-Day Daten
        parameter = {
            'access_key': self.API_Key,
            'symbols': ticker,              # Der Ticker einer bestimmten Aktie
            'date_from': date_from,         # "Von"-Datum: "YYYY-MM-DD" oder im ISO-8601 Datum Format (bis zu 30 Jahre)
            'date_to': date_to              # "Bis"-Datum: "YYYY-MM-DD" oder im ISO-8601 Datum Format
        }
        api_ergebnis = requests.get('http://api.marketstack.com/v1/eod', parameter)  # HTTP GET Request
        return api_ergebnis.json()

