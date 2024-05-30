import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FONT_SIZE = 36

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dictator Game')
font = pygame.font.Font(None, FONT_SIZE)

# Variables
endowment = 100
dictator_share = endowment
recipient_share = 0

# Buttons
buttons = {
    'decrease_dictator': pygame.Rect(100, 300, 200, 50),
    'increase_dictator': pygame.Rect(500, 300, 200, 50),
    'confirm': pygame.Rect(300, 450, 200, 50)
}

# Button texts
button_texts = {
    'decrease_dictator': font.render('Give More', True, BLACK),
    'increase_dictator': font.render('Give Less', True, BLACK),
    'confirm': font.render('Confirm', True, BLACK)
}

def draw_ui():
    screen.fill(WHITE)
    endowment_text = font.render(f"Endowment: ${endowment}", True, BLACK)
    dictator_text = font.render(f"Dictator's Share: ${dictator_share}", True, BLUE)
    recipient_text = font.render(f"Recipient's Share: ${recipient_share}", True, RED)
    screen.blit(endowment_text, (SCREEN_WIDTH // 2 - endowment_text.get_width() // 2, 50))
    screen.blit(dictator_text, (100, 200))
    screen.blit(recipient_text, (500, 200))
    for key, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        text = button_texts[key]
        screen.blit(text, (rect.x + (rect.width - text.get_width()) // 2, rect.y + (rect.height - text.get_height()) // 2))

# Main game loop
running = True
decision_made = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not decision_made:
            mouse_pos = event.pos
            if buttons['decrease_dictator'].collidepoint(mouse_pos):
                if dictator_share > 0:
                    dictator_share -= 10
                    recipient_share += 10
            elif buttons['increase_dictator'].collidepoint(mouse_pos):
                if recipient_share > 0:
                    dictator_share += 10
                    recipient_share -= 10
            elif buttons['confirm'].collidepoint(mouse_pos):
                decision_made = True

    draw_ui()
    if decision_made:
        result_text = font.render(f"Decision Made! Dictator: ${dictator_share}, Recipient: ${recipient_share}", True, BLACK)
        screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
