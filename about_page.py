from PyQt5 import QtWidgets, uic

class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        uic.loadUi('ui/about_ui.ui', self)
        self.show()



from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = AboutWindow()
app.exec_()