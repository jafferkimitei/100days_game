from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window  # Import Window for keyboard handling
import random
import time

class SnakePart(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.size = (20, 20)
        self.pos = pos
        with self.canvas:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def move(self, new_pos):
        self.pos = new_pos
        self.rect.pos = self.pos

class Food(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.size = (20, 20)
        self.pos = pos
        with self.canvas:
            Color(1, 0, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)

class SnakeGame(Widget):
    def __init__(self, game_mode='easy', **kwargs):
        super().__init__(**kwargs)
        self.snake = []
        self.food = None
        self.direction = 'right'
        self.paused = False
        self.score = 0
        self.game_mode = game_mode
        self.speed = {'easy': 0.3, 'medium': 0.2, 'hard': 0.1}[self.game_mode]
        self.create_snake()
        self.create_food()
        self.score_label = Label(text=f"Score: {self.score}", pos=(10, Window.height - 40))
        self.add_widget(self.score_label)
        Clock.schedule_interval(self.update, self.speed)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'spacebar':
            self.paused = not self.paused
        elif keycode[1] in ['up', 'down', 'left', 'right']:
            self.direction = keycode[1]

    def create_snake(self):
        self.snake.append(SnakePart((100, 100)))
        self.snake.append(SnakePart((80, 100)))
        self.snake.append(SnakePart((60, 100)))
        for part in self.snake:
            self.add_widget(part)

    def create_food(self):
        while True:
            food_pos = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)
            if food_pos not in [part.pos for part in self.snake]:
                break
        self.food = Food(food_pos)
        self.add_widget(self.food)

    def update(self, dt):
        if self.paused:
            return
        
        head = self.snake[0]
        new_pos = list(head.pos)
        
        if self.direction == 'up':
            new_pos[1] += 20
        elif self.direction == 'down':
            new_pos[1] -= 20
        elif self.direction == 'left':
            new_pos[0] -= 20
        elif self.direction == 'right':
            new_pos[0] += 20
        
        if new_pos[0] < 0 or new_pos[0] >= Window.width or new_pos[1] < 0 or new_pos[1] >= Window.height or any(part.pos == tuple(new_pos) for part in self.snake):
            self.game_over()
            return

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].move(self.snake[i-1].pos)
        head.move(tuple(new_pos))

        if head.pos == self.food.pos:
            self.snake.append(SnakePart(self.snake[-1].pos))
            self.remove_widget(self.food)
            self.create_food()
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

    def game_over(self):
        Clock.unschedule(self.update)
        self.add_widget(Label(text="Game Over", font_size=48, center=self.center))
        self.add_widget(Label(text=f"Final Score: {self.score}", font_size=32, pos=(Window.width // 2 - 70, Window.height // 2 - 70)))

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text="Loading...", font_size=32))
        self.add_widget(layout)

    def on_enter(self, *args):
        # Simulate loading time
        Clock.schedule_once(self.go_to_difficulty_screen, 2)

    def go_to_difficulty_screen(self, dt):
        self.manager.current = 'difficulty'

class DifficultyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.mode = 'easy'  # Default mode
        
        layout.add_widget(Label(text="Select Game Mode:", font_size=24))
        
        self.easy_button = Button(text="Easy", font_size=24)
        self.easy_button.bind(on_press=self.set_easy_mode)
        layout.add_widget(self.easy_button)
        
        self.medium_button = Button(text="Medium", font_size=24)
        self.medium_button.bind(on_press=self.set_medium_mode)
        layout.add_widget(self.medium_button)
        
        self.hard_button = Button(text="Hard", font_size=24)
        self.hard_button.bind(on_press=self.set_hard_mode)
        layout.add_widget(self.hard_button)
        
        continue_button = Button(text="Continue", font_size=24)
        continue_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(continue_button)
        
        self.add_widget(layout)
    
    def set_easy_mode(self, instance):
        self.mode = 'easy'
    
    def set_medium_mode(self, instance):
        self.mode = 'medium'
    
    def set_hard_mode(self, instance):
        self.mode = 'hard'
    
    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'
        self.manager.get_screen('main_menu').mode = self.mode

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mode = 'easy'  # Default mode
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        play_button = Button(text="Play", font_size=24)
        play_button.bind(on_press=self.play_game)
        layout.add_widget(play_button)
        
        quit_button = Button(text="Quit", font_size=24)
        quit_button.bind(on_press=App.get_running_app().stop)
        layout.add_widget(quit_button)
        
        self.add_widget(layout)
    
    def play_game(self, instance):
        self.manager.current = 'game'
        self.manager.get_screen('game').start_game(self.mode)

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = None
    
    def start_game(self, mode):
        if self.game:
            self.remove_widget(self.game)
        self.game = SnakeGame(game_mode=mode)
        self.add_widget(self.game)

class SnakeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(DifficultyScreen(name='difficulty'))
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    SnakeApp().run()
