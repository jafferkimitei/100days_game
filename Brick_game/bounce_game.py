import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BRICK_WIDTH = 75
BRICK_HEIGHT = 30
ROW_COUNT = 5
COLUMN_COUNT = 10
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Brick Breaker')

# Paddle setup
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = 4, -4

# Brick setup
bricks = []
for row in range(ROW_COUNT):
    for col in range(COLUMN_COUNT):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5) + 35, row * (BRICK_HEIGHT + 5) + 35, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Score and Lives
score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Main game loop
running = True
paused = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= 5
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.right += 5

        # Ball movement
        ball.left += ball_dx
        ball.top += ball_dy

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_dx *= -1
        if ball.top <= 0:
            ball_dy *= -1
        if ball.bottom >= SCREEN_HEIGHT:
            lives -= 1
            ball.left, ball.top = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx, ball_dy = 4, -4
            if lives == 0:
                running = False

        # Ball collision with paddle
        if ball.colliderect(paddle):
            ball_dy *= -1

        # Ball collision with bricks
        hit_index = ball.collidelist(bricks)
        if hit_index != -1:
            brick = bricks[hit_index]
            if abs(ball.bottom - brick.top) < 10 or abs(ball.top - brick.bottom) < 10:
                ball_dy *= -1
            else:
                ball_dx *= -1
            del bricks[hit_index]
            score += 1
            if not bricks:
                running = False

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (5, 5))
    screen.blit(lives_text, (SCREEN_WIDTH - 100, 5))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
