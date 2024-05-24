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

# Game variables
deck = [(suit, value) for suit in ['hearts', 'diamonds', 'clubs', 'spades'] for value in range(1, 14)]
random.shuffle(deck)

# Function to draw a card
def draw_card(card, x, y):
    screen.blit(card_images[card], (x, y))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw cards from the deck
    if len(deck) > 0:
        draw_card(deck[-1], 50, 50)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
