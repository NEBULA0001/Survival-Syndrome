import pygame
import random
from gui import render_text, render_BOXgui
from player import Player

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
pygame.display.set_caption("Survival Syndrome BETA")
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = Player(100, player_pos, 10)

font = pygame.font.Font(None, big_font_size)
small_font = pygame.font.Font(None, small_font_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GAME_BG_color)

    # RENDER YOUR GAME HERE
    player.drawPlayer(screen)   
    player.update(dt)

    render_text(screen, "RUST 2D V1.0 BETA", font, (255, 255, 255), (10, 10))
    render_BOXgui(screen, (200, 80), "Health", (150, 100, 0), (0, 520))

    pygame.display.flip()

    dt = clock.tick(GAME_FPS) / 1000

pygame.quit()