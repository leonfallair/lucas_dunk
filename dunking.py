import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Leon dunkt über Lucas")

# Farben
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
BLUE = (50, 150, 255)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

# Figurenpositionen
leon_x, leon_y = 300, 400
lucas_x, lucas_y = 450, 420
ball_y = leon_y - 40

# Font
font = pygame.font.SysFont("Arial", 24)

# Animationseinstellungen
clock = pygame.time.Clock()
jumping = True
frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Basketball-Court zeichnen
    pygame.draw.rect(screen, BROWN, (0, HEIGHT - 100, WIDTH, 100))

    # Namen
    screen.blit(font.render("Leon", True, BLACK), (leon_x - 10, leon_y - 60))
    screen.blit(font.render("Lucas", True, BLACK), (lucas_x - 10, lucas_y - 60))

    # Figuren zeichnen (Körper als Rechtecke)
    pygame.draw.rect(screen, RED, (leon_x, leon_y - 80, 30, 80))     # Leon
    pygame.draw.rect(screen, BLUE, (lucas_x, lucas_y - 70, 25, 70))  # Lucas

    # Leon springt (Dunk-Animation)
    if jumping:
        if frame < 40:
            leon_y -= 4
            ball_y -= 4
        elif frame < 80:
            leon_y += 4
            ball_y += 4
        else:
            jumping = False
        frame += 1

    # Ball zeichnen
    pygame.draw.circle(screen, (255, 165, 0), (leon_x + 15, ball_y), 10)

    pygame.display.flip()
    clock.tick(30)
