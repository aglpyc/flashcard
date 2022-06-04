from PyQt5 import QtWidgets, uic

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('ui/login_ui.ui', self)
        self.show()