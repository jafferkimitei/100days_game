import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 71, 96
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solitaire")

# Load card images
card_images = {}
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for value in range(1, 14):
        card_images[(suit, value)] = pygame.image.load(f'cards/{value}_of_{suit}.png')

# Function to draw a card
def draw_card(card, x, y):
    screen.blit(card_images[card], (x, y))

# Function to check if a card is clicked
def is_clicked(card_rect, pos):
    return card_rect.collidepoint(pos)

# Main game loop
running = True
clock = pygame.time.Clock()

# Sample deck and tableau for demonstration purposes
deck = [(suit, value) for suit in ['hearts', 'diamonds', 'clubs', 'spades'] for value in range(1, 14)]
random.shuffle(deck)

tableau = [[deck.pop() for _ in range(i)] for i in range(1, 8)]

# Dictionary to store card positions and rectangles
card_rects = {}
for i, column in enumerate(tableau):
    for j, card in enumerate(column):
        card_rects[card] = pygame.Rect(50 + i * (CARD_WIDTH + 10), 150 + j * 20, CARD_WIDTH, CARD_HEIGHT)

# Dragging variables
selected_card = None
dragging = False
offset_x, offset_y = 0, 0

while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is on a card
            for card, rect in card_rects.items():
                if is_clicked(rect, event.pos):
                    selected_card = card
                    offset_x = event.pos[0] - rect.x
                    offset_y = event.pos[1] - rect.y
                    dragging = True
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_card = None
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Move the selected card with the mouse
            if dragging:
                card_rects[selected_card].x = event.pos[0] - offset_x
                card_rects[selected_card].y = event.pos[1] - offset_y

    # Draw the cards
    for card, rect in card_rects.items():
        screen.blit(card_images[card], rect)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
