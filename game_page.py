from PyQt5 import QtWidgets, uic
import menu_page
from flashcard_game import Game
from PyQt5.QtCore import QTimer

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self, object):
        self.object = object
        self.game = Game(self.object)
        self.game.starting_time()
        super(GameWindow, self).__init__()
        uic.loadUi('ui/game_ui.ui', self)
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.back_button.clicked.connect(self.menu_show)
        self.exit_button.clicked.connect(self.exit)
        self.true_button.clicked.connect(self.true_button_function) 
        self.false_button.clicked.connect(self.false_button_function)
        self.timer_()
        self.show()

    def menu_show(self):
        self.passedTime = int(self.game.totalTime())
        self.object.registerUserStat(self.object.level, self.passedTime)
        self.cams = menu_page.MainWindow(self.object)
        self.cams.show()
        self.close()
           
    def update(self):
        self.timelabel.setText(str(self.count))
        if self.count == 0:
            self.true_button.setEnabled(True)
            self.false_button.setEnabled(True)
            self.timer.stop()
            self.en_word(self.word_en)
        self.count -= 1
            
    def en_word(self, en):
        self.en = en
        self.language_label.setText("ENGLISH")
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 220);\nborder-color: rgb(170, 85, 0);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.word_label.setText(self.en)
        
    def timer_(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count = 0
        self.starting()
        
    def false_word(self):
        self.totalTry_num = self.game.total_attempt_number()
        self.try_label.setText(str(self.totalTry_num))                                                                   
    
    def starting(self):
        self.word_nl, self.word_en, self.true_num = self.game.show_words()
        self.totalTry_num=self.game.attempts_number
        self.label_2.setStyleSheet("background-color:rgb(5, 119, 161);\nborder-color: rgb(170, 85, 0);\nborder-style: solid;\nborder-width: 3px;\nborder-radius:50px;")
        self.level_label.setText("LEVEL " + str(self.object.level))
        self.language_label.setText("NEDERLANDS")
        self.true_label.setText(str(self.true_num))
        self.progressBar.setProperty('value',self.true_num)
        self.true_button.setEnabled(False)
        self.false_button.setEnabled(False)
        self.word_label.setText(self.word_nl)
        self.try_label.setText(str(self.totalTry_num))
    
    def true_button_function(self):
        self.game.total_attempt_number()
        self.game.true()
        self.timer_()
        
    def false_button_function(self):
        self.game.total_attempt_number()
        self.game.false()
        self.timer_()
           
    def exit(self):
        self.passedTime = self.game.totalTime()
        self.object.registerUserStat(self.object.level, self.passedTime)
        self.close()