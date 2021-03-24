"""
main.py -> Die main Methode des Börsenspiels.
"""

import SPIELER as S
import UI
import MARKETSTACK as M

def main():
    spieler = S.SPIELER()
    ui      = UI.UI()
    api     = M.MARKETSTACK()


if __name__ == "__main__":
    main()
