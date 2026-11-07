import pygame
import random
from gui import *

HEIGHT = 800
WIDTH = 600

# Game settings
GAME_FPS = 60
GAME_BG_color = (0, 125, 0)
GAME_PLAYER_color = (255, 0, 0)

#visuals gui related
big_font_size = 36
small_font_size = 12

#actual game code
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.Font(None, big_font_size)
small_font = pygame.font.Font(None, small_font_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GAME_BG_color)

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, GAME_PLAYER_color, player_pos, 30)

    render_text(screen, "RUST 2D V1.0 BETA", font, (255, 255, 255), (10, 10))
    render_GUI_Box(screen, (250, 80), "Inventory", (150, 100, 0), (0, 520))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    pygame.display.flip()

    dt = clock.tick(GAME_FPS) / 1000

pygame.quit()