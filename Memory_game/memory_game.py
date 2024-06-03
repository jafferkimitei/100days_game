import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_SIZE = 100
GRID_SIZE = 4
PADDING = 20
FONT_SIZE = 36
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Memory Game')
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

# Load card images
card_images = [pygame.Surface((CARD_SIZE, CARD_SIZE)) for _ in range(GRID_SIZE * GRID_SIZE // 2)]
for i, card in enumerate(card_images):
    card.fill(GREEN)
    pygame.draw.circle(card, BLACK, (CARD_SIZE // 2, CARD_SIZE // 2), CARD_SIZE // 4)

# Duplicate card images to create pairs
cards = card_images * 2
random.shuffle(cards)

# Variables
grid = []
for row in range(GRID_SIZE):
    grid_row = []
    for col in range(GRID_SIZE):
        card_rect = pygame.Rect(col * (CARD_SIZE + PADDING), row * (CARD_SIZE + PADDING), CARD_SIZE, CARD_SIZE)
        grid_row.append({"rect": card_rect, "image": cards.pop(), "flipped": False, "matched": False})
    grid.append(grid_row)

first_card = None
second_card = None
matched_pairs = 0

def draw_grid():
    screen.fill(WHITE)
    for row in grid:
        for card in row:
            if card["flipped"] or card["matched"]:
                screen.blit(card["image"], card["rect"].topleft)
            else:
                pygame.draw.rect(screen, GRAY, card["rect"])
    pygame.display.flip()

def check_for_match():
    global first_card, second_card, matched_pairs
    if first_card["image"] == second_card["image"]:
        first_card["matched"] = True
        second_card["matched"] = True
        matched_pairs += 1
    else:
        pygame.time.wait(1000)
        first_card["flipped"] = False
        second_card["flipped"] = False
    first_card = None
    second_card = None

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for row in grid:
                for card in row:
                    if card["rect"].collidepoint(mouse_pos) and not card["flipped"] and not card["matched"]:
                        card["flipped"] = True
                        if first_card is None:
                            first_card = card
                        elif second_card is None:
                            second_card = card
                            check_for_match()

    draw_grid()
    clock.tick(FPS)

pygame.quit()
sys.exit()
