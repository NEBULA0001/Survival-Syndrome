import pygame
import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "../assets/Player/Player.png")

class Player:
    def __init__(self, health, player_pos, damage):
        self.health = health
        self.player_pos = player_pos
        self.damage = damage

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=self.player_pos)
    
    def __Str__(self):
        return self.health
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Adjust the speed value (e.g., 300) to make them move faster or slower
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt

        self.rect.center = (int(self.player_pos.x), int(self.player_pos.y))
    
    def drawPlayer(self, screen):
        screen.blit(self.image, self.rect)