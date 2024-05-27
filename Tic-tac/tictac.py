from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class TicTacToeApp(App):
    def build(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        
        self.layout = GridLayout(cols=3, rows=3)
        
        self.buttons = []
        for i in range(9):
            button = Button(font_size=32, on_press=self.on_button_press)
            self.buttons.append(button)
            self.layout.add_widget(button)
        
        return self.layout
    
    def on_button_press(self, instance):
        index = self.buttons.index(instance)
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            instance.text = self.current_player
            
            if self.check_winner(self.current_player):
                self.show_popup(f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                self.show_popup("It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
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
