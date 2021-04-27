"""
main.py -> Die main Funktion des Börsenspiels.
"""

import src.SPIELER as S
import src.MARKETSTACK as M

from ui.main_window import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


def main():
    spieler = S.SPIELER('Bob')
    api = M.MARKETSTACK()


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Hier können die Methoden mit den Widgets verbunden werden
        self.ui.pushButton.clicked.connect(self.drucke)

    # Hier die Methoden für Funktionen der Widgets (z.B. Button) einfügen
    def drucke(self):
        print(self.ui.textEdit.toPlainText())


if __name__ == "__main__":
    main()

    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()
