from PyQt5 import QtWidgets, uic

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        uic.loadUi('ui/game_ui.ui', self)
        self.show()