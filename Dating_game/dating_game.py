import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox

class DatingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dating Game')

        self.layout = QVBoxLayout()

        self.story_label = QLabel('Welcome to the dating game! You are at a party and see three interesting people...')
        self.layout.addWidget(self.story_label)

        self.choice1_button = QPushButton('Talk to Person A', self)
        self.choice1_button.clicked.connect(self.talk_to_person_a)
        self.layout.addWidget(self.choice1_button)

        self.choice2_button = QPushButton('Talk to Person B', self)
        self.choice2_button.clicked.connect(self.talk_to_person_b)
        self.layout.addWidget(self.choice2_button)
        
        self.choice3_button = QPushButton('Talk to Person C', self)
        self.choice3_button.clicked.connect(self.talk_to_person_c)
        self.layout.addWidget(self.choice3_button)

        self.setLayout(self.layout)

    def talk_to_person_a(self):
        self.story_label.setText('You chose to talk to Person A. They are charming and you enjoy your conversation...')
        self.choice1_button.setText('Ask about their hobbies')
        self.choice1_button.clicked.connect(self.ask_hobbies_a)
        self.choice2_button.setText('Ask for their number')
        self.choice2_button.clicked.connect(self.ask_number_a)
        self.choice3_button.setText('Talk to Person B')
        self.choice3_button.clicked.connect(self.talk_to_person_b)

    def ask_hobbies_a(self):
        self.story_label.setText('Person A loves painting and hiking. You both share your interests and bond over common hobbies...')
        self.choice1_button.setText('Ask for their number')
        self.choice1_button.clicked.connect(self.ask_number_a)
        self.choice2_button.setText('Talk to Person B')
        self.choice2_button.clicked.connect(self.talk_to_person_b)
        self.choice3_button.setText('Talk to Person C')
        self.choice3_button.clicked.connect(self.talk_to_person_c)

    def ask_number_a(self):
        reply = QMessageBox.question(self, 'Ask for Number',
                                     "Person A is impressed and gives you their number. Do you want to call them now?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.story_label.setText('You call Person A and have a great conversation. You decide to go on a date. Congratulations!')
            self.choice1_button.setText('Restart')
            self.choice1_button.clicked.connect(self.initUI)
            self.choice2_button.setText('Exit')
            self.choice2_button.clicked.connect(self.close)
            self.choice3_button.hide()
        else:
            self.story_label.setText('You decide to call Person A later. The party continues...')
            self.choice1_button.setText('Talk to Person B')
            self.choice1_button.clicked.connect(self.talk_to_person_b)
            self.choice2_button.setText('Talk to Person C')
            self.choice2_button.clicked.connect(self.talk_to_person_c)
            self.choice3_button.setText('Exit')
            self.choice3_button.clicked.connect(self.close)

    def talk_to_person_b(self):
        self.story_label.setText('You chose to talk to Person B. They are witty and you have a great time together...')
        self.choice1_button.setText('Ask about their job')
        self.choice1_button.clicked.connect(self.ask_job_b)
        self.choice2_button.setText('Ask for their number')
        self.choice2_button.clicked.connect(self.ask_number_b)
        self.choice3_button.setText('Talk to Person C')
        self.choice3_button.clicked.connect(self.talk_to_person_c)

    def ask_job_b(self):
        self.story_label.setText('Person B works as a software developer. You both discuss your careers and share interesting stories...')
        self.choice1_button.setText('Ask for their number')
        self.choice1_button.clicked.connect(self.ask_number_b)
        self.choice2_button.setText('Talk to Person A')
        self.choice2_button.clicked.connect(self.talk_to_person_a)
        self.choice3_button.setText('Talk to Person C')
        self.choice3_button.clicked.connect(self.talk_to_person_c)

    def ask_number_b(self):
        reply = QMessageBox.question(self, 'Ask for Number',
                                     "Person B is impressed and gives you their number. Do you want to call them now?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.story_label.setText('You call Person B and have a great conversation. You decide to go on a date. Congratulations!')
            self.choice1_button.setText('Restart')
            self.choice1_button.clicked.connect(self.initUI)
            self.choice2_button.setText('Exit')
            self.choice2_button.clicked.connect(self.close)
            self.choice3_button.hide()
        else:
            self.story_label.setText('You decide to call Person B later. The party continues...')
            self.choice1_button.setText('Talk to Person A')
            self.choice1_button.clicked.connect(self.talk_to_person_a)
            self.choice2_button.setText('Talk to Person C')
            self.choice2_button.clicked.connect(self.talk_to_person_c)
            self.choice3_button.setText('Exit')
            self.choice3_button.clicked.connect(self.close)

    def talk_to_person_c(self):
        self.story_label.setText('You chose to talk to Person C. They are funny and you enjoy your conversation...')
        self.choice1_button.setText('Ask about their travels')
        self.choice1_button.clicked.connect(self.ask_travels_c)
        self.choice2_button.setText('Ask for their number')
        self.choice2_button.clicked.connect(self.ask_number_c)
        self.choice3_button.setText('Talk to Person A')
        self.choice3_button.clicked.connect(self.talk_to_person_a)

    def ask_travels_c(self):
        self.story_label.setText('Person C loves traveling and has been to many exciting places. You both share travel stories...')
        self.choice1_button.setText('Ask for their number')
        self.choice1_button.clicked.connect(self.ask_number_c)
        self.choice2_button.setText('Talk to Person A')
        self.choice2_button.clicked.connect(self.talk_to_person_a)
        self.choice3_button.setText('Talk to Person B')
        self.choice3_button.clicked.connect(self.talk_to_person_b)

    def ask_number_c(self):
        reply = QMessageBox.question(self, 'Ask for Number',
                                     "Person C is impressed and gives you their number. Do you want to call them now?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.story_label.setText('You call Person C and have a great conversation. You decide to go on a date. Congratulations!')
            self.choice1_button.setText('Restart')
            self.choice1_button.clicked.connect(self.initUI)
            self.choice2_button.setText('Exit')
            self.choice2_button.clicked.connect(self.close)
            self.choice3_button.hide()
        else:
            self.story_label.setText('You decide to call Person C later. The party continues...')
            self.choice1_button.setText('Talk to Person A')
            self.choice1_button.clicked.connect(self.talk_to_person_a)
            self.choice2_button.setText('Talk to Person B')
            self.choice2_button.clicked.connect(self.talk_to_person_b)
            self.choice3_button.setText('Exit')
            self.choice3_button.clicked.connect(self.close)

def main():
    app = QApplication(sys.argv)
    game = DatingGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
