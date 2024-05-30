from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Ellipse, Color
from kivy.core.window import Window
from kivy.clock import Clock

class Paddle(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (100, 20)
        self.pos = (Window.width / 2 - self.width / 2, 50)
        with self.canvas:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    
    def move(self, new_pos):
        self.pos = new_pos
        self.rect.pos = self.pos

class Ball(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (20, 20)
        self.pos = (Window.width / 2 - self.width / 2, Window.height / 2 - self.height / 2)
        self.velocity = [4, -4]
        with self.canvas:
            Color(1, 0, 0)
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
    
    def move(self):
        self.pos = (self.x + self.velocity[0], self.y + self.velocity[1])
        self.ellipse.pos = self.pos

class Brick(Widget):
    def __init__(self, pos, **kwargs):
        super().__init__(**kwargs)
        self.size = (80, 30)
        self.pos = pos
        with self.canvas:
            Color(0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

class BrickGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.paddle = Paddle()
        self.add_widget(self.paddle)
        self.ball = Ball()
        self.add_widget(self.ball)
        self.bricks = []
        self.create_bricks()
        self.score = 0
        self.lives = 3
        self.score_label = Label(text=f"Score: {self.score}", pos=(10, Window.height - 40))
        self.add_widget(self.score_label)
        self.lives_label = Label(text=f"Lives: {self.lives}", pos=(Window.width - 100, Window.height - 40))
        self.add_widget(self.lives_label)
        Clock.schedule_interval(self.update, 1 / 60)
        Window.bind(on_key_down=self.on_key_down)
        self.paused = False

    def create_bricks(self):
        for row in range(5):
            for col in range(10):
                brick = Brick(pos=(col * 80, Window.height - (row + 1) * 30 - 50))
                self.bricks.append(brick)
                self.add_widget(brick)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 276:  # Left arrow
            new_x = max(self.paddle.x - 20, 0)
            self.paddle.move((new_x, self.paddle.y))
        elif keycode == 275:  # Right arrow
            new_x = min(self.paddle.x + 20, Window.width - self.paddle.width)
            self.paddle.move((new_x, self.paddle.y))
        elif keycode == 32:  # Space bar
            self.paused = not self.paused

    def update(self, dt):
        if self.paused:
            return
        
        self.ball.move()

        # Ball collision with walls
        if self.ball.x <= 0 or self.ball.right >= Window.width:
            self.ball.velocity[0] *= -1
        if self.ball.top >= Window.height:
            self.ball.velocity[1] *= -1
        if self.ball.y <= 0:
            self.lives -= 1
            self.lives_label.text = f"Lives: {self.lives}"
            if self.lives == 0:
                self.game_over()
            else:
                self.ball.pos = (Window.width / 2 - self.ball.width / 2, Window.height / 2 - self.ball.height / 2)
                self.ball.velocity = [4, -4]

        # Ball collision with paddle
        if self.ball.collide_widget(self.paddle):
            self.ball.velocity[1] *= -1

        # Ball collision with bricks
        for brick in self.bricks:
            if self.ball.collide_widget(brick):
                self.bricks.remove(brick)
                self.remove_widget(brick)
                self.ball.velocity[1] *= -1
                self.score += 1
                self.score_label.text = f"Score: {self.score}"
                if not self.bricks:
                    self.win()

    def game_over(self):
        self.paused = True
        self.add_widget(Label(text="Game Over", font_size=48, center=self.center))

    def win(self):
        self.paused = True
        self.add_widget(Label(text="You Win!", font_size=48, center=self.center))

class BrickGameApp(App):
    def build(self):
        return BrickGame()

if __name__ == '__main__':
    BrickGameApp().run()
