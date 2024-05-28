from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window  
import random

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = []
        self.food = None
        self.direction = 'right'
        self.score = 0
        self.create_snake()
        self.create_food()
        self.score_label = Label(text=f"Score: {self.score}", pos=(10, Window.height - 40))
        self.add_widget(self.score_label)
        Clock.schedule_interval(self.update, 0.2)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ['up', 'down', 'left', 'right']:
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

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
