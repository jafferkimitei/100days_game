from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

class TicTacToeApp(App):
    def build(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.difficulty_level = None
        
        self.layout = GridLayout(cols=1)
        
        self.difficulty_label = Label(text="Choose Difficulty Level:", font_size=24)
        self.layout.add_widget(self.difficulty_label)
        
        self.easy_button = Button(text="Easy", on_press=self.set_easy_difficulty)
        self.layout.add_widget(self.easy_button)
        
        self.medium_button = Button(text="Medium", on_press=self.set_medium_difficulty)
        self.layout.add_widget(self.medium_button)
        
        self.hard_button = Button(text="Hard", on_press=self.set_hard_difficulty)
        self.layout.add_widget(self.hard_button)
        
        return self.layout
    
    def set_easy_difficulty(self, instance):
        self.difficulty_level = 'Easy'
        self.start_game()
    
    def set_medium_difficulty(self, instance):
        self.difficulty_level = 'Medium'
        self.start_game()
    
    def set_hard_difficulty(self, instance):
        self.difficulty_level = 'Hard'
        self.start_game()
    
    def start_game(self):
        self.layout.clear_widgets()
        
        grid_layout = GridLayout(cols=3, rows=3)
        
        self.buttons = []
        for i in range(9):
            button = Button(font_size=32, on_press=self.on_button_press)
            self.buttons.append(button)
            grid_layout.add_widget(button)
        
        self.layout.add_widget(grid_layout)
        
        if self.current_player == 'O' and self.difficulty_level == 'Hard':
            self.hard_computer_move()
    
    def on_button_press(self, instance):
        index = self.buttons.index(instance)
        if self.board[index] == ' ':
            self.board[index] = 'X'
            instance.text = 'X'
            
            if self.check_winner('X'):
                self.show_popup("You win!")
                self.reset_board()
                return
            elif self.check_draw():
                self.show_popup("It's a draw!")
                self.reset_board()
                return
            
            # Computer's turn
            if self.difficulty_level == 'Easy':
                self.easy_computer_move()
            elif self.difficulty_level == 'Medium':
                self.medium_computer_move()
            elif self.difficulty_level == 'Hard':
                self.hard_computer_move()
            
            if self.check_winner('O'):
                self.show_popup("Computer wins!")
                self.reset_board()
                return
            elif self.check_draw():
                self.show_popup("It's a draw!")
                self.reset_board()
                return
    
    def easy_computer_move(self):
        empty_cells = [i for i, mark in enumerate(self.board) if mark == ' ']
        if empty_cells:
            index = random.choice(empty_cells)
            self.board[index] = 'O'
            self.buttons[index].text = 'O'
    
    def medium_computer_move(self):
        # Implement medium difficulty move here
        empty_cells = [i for i, mark in enumerate(self.board) if mark == ' ']
        if empty_cells:
            index = random.choice(empty_cells)
            self.board[index] = 'O'
            self.buttons[index].text = 'O'
    
    def hard_computer_move(self):
        # Implement hard difficulty move here
        best_score = float('-inf')
        best_move = None
        
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, False)
                self.board[i] = ' '  # Undo the move
                
                if score > best_score:
                    best_score = score
                    best_move = i
        
        self.board[best_move] = 'O'
        self.buttons[best_move].text = 'O'
    
    def minimax(self, board, is_maximizing):
        if self.check_winner('O'):
            return 1
        elif self.check_winner('X'):
            return -1
        elif self.check_draw():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, False)
                    board[i] = ' '  # Undo the move
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, True)
                    board[i] = ' '  # Undo the move
                    best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False
    
    def check_draw(self):
        return ' ' not in self.board
    
    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.text = ''
    
    def show_popup(self, message):
        popup = Popup(title='Game Over', content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()

if __name__ == '__main__':
    TicTacToeApp().run()
