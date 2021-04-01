"""
main.py -> Die main Funktion des Börsenspiels.
"""

import SPIELER as S
import UI
import MARKETSTACK as M


def main():
    spieler = S.SPIELER('Elias')
    ui = UI.UI()
    api = M.MARKETSTACK()

    print('Fertig.')


if __name__ == "__main__":
    main()
