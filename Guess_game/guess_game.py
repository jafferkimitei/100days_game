import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QWidget

class GuessingGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guessing Game")
        self.setGeometry(100, 100, 300, 250)
        
        self.words = {
            'Easy': [('cat', 'A common household pet'), 
                     ('dog', 'Man\'s best friend'), 
                     ('fish', 'Lives in water')],
            'Medium': [('elephant', 'Largest land animal'), 
                       ('giraffe', 'Tallest land animal'), 
                       ('crocodile', 'Large aquatic reptile')],
            'Hard': [('chimpanzee', 'Closest relative to humans'), 
                     ('hippopotamus', 'Large, mostly herbivorous mammal in sub-Saharan Africa'), 
                     ('rhinoceros', 'Large, herbivorous mammal with one or two horns on its snout')]
        }
        
        self.current_word = ''
        self.current_hint = ''
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Select difficulty and start the game")
        self.layout.addWidget(self.label)
        
        self.hint_label = QLabel("")
        self.layout.addWidget(self.hint_label)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(self.words.keys())
        self.layout.addWidget(self.combo_box)
        
        self.start_button = QPushButton("Start Game")
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
        
        self.input = QLineEdit()
        self.layout.addWidget(self.input)
        
        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.guess_button)
        
        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def start_game(self):
        difficulty = self.combo_box.currentText()
        self.current_word, self.current_hint = random.choice(self.words[difficulty])
        self.label.setText(f"Guess the word ({len(self.current_word)} letters)")
        self.hint_label.setText(f"Hint: {self.current_hint}")
        self.result_label.setText("")
        self.input.setText("")
    
    def check_guess(self):
        guess = self.input.text().strip()
        if guess == self.current_word:
            self.result_label.setText("Correct! You guessed the word!")
        else:
            self.result_label.setText("Incorrect, try again.")

def main():
    app = QApplication(sys.argv)
    game = GuessingGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
