"""
DATEN.py -> Die Klasse DATEN und MARKETSTACK, die den Zugriff auf die marketstack.com API koordiniert und damit auch das Erhalten und
Aufbereiten von Aktiendaten.
"""
import src.BINAERBAUM as b

import requests
import platform
import subprocess
import pandas_datareader as pdr
from datetime import date, timedelta
import random


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
        self.tickerbaum = b.BINAERBAUM('tickers', 'name')
        self.aktiendatenCache = {}

    def tickerErneuern( self ):
        frame = pdr.get_iex_symbols()
        liste = []
        for ind, val in enumerate(frame['symbol']):
            liste.append({
                'symbol': val,
                'name': frame['name'][ind],
                'type': frame['type'][ind]
            })
        self.tickerbaum.bauBaumAusListe(liste)

    def tickerpreisErhalten( self, ticker: str, von="1980-12-12", bis="heute", key="Adj Close" ) -> 'DataFrame':
        #TODO Sichern im Cache
        if bis == "heute":
            bis = date.today()
        if von == "heute":
            von = date.today()
        return pdr.DataReader(ticker, "yahoo", start=von, end=bis)[key]

    def tickerpreisErhaltenInTagen( self, ticker: str, tage: int ):
        von_Datum = date.today() - timedelta(days=tage)
        return self.tickerpreisErhalten(ticker, von=von_Datum)

    def aktuellenTickerpreisErhalten( self, ticker: str):
        #TODO Von $ nach € umwandeln
        return pdr.DataReader(ticker, "iex-last", pause=0)[0]['price']

    def aktiennameErhalten( self, ticker: str) -> str:
        liste = self.tickerbaum.inOrderAusgeben()
        for element in liste:
            if element['symbol'] == ticker:
                return element['name']
        return ""