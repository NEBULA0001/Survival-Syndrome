import pygame
import os
import math

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "../assets/Player/Player.png")

player_health = 100
player_speed = 150

class Player:
    def __init__(self, health, player_pos, damage):
        self.health = health
        self.player_pos = pygame.math.Vector2(player_pos) # Ensure it's a vector
        self.damage = damage

        # Keep a pristine copy of the original image for clean scaling/rotations
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (64, 64))
        
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.player_pos)
        
        # Sway variables
        self.is_moving = False
        self.anim_time = 0.0

    def __str__(self):
        return str(self.health)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        moved = False
        
        # Track movement direction for the velocity vector
        direction = pygame.math.Vector2(0, 0)
        
        # Fixed: Removed the redundant speed * dt multipliers here
        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_s]:
            direction.y += 1
        if keys[pygame.K_a]:
            direction.x -= 1
        if keys[pygame.K_d]:
            direction.x += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.player_pos += direction * player_speed * dt
            moved = True

        # Handle sway / tilt and scaling animation
        if moved:
            self.anim_time += dt * 10  # Adjust speed of the animation cycle if needed
            tilt_angle = math.sin(self.anim_time) * 8
            
            # Pulse size: uses absolute cosine to create a smooth squash/stretch bounce (ranges from 1.0 to ~1.12 scale)
            scale_factor = 1.0 + abs(math.cos(self.anim_time)) * 0.12
        else:
            # Smoothly reset when stopped
            self.anim_time = 0.0
            tilt_angle = 0
            scale_factor = 1.0

        # Apply scaling and rotation from the original pristine image
        base_size = 64
        new_size = int(base_size * scale_factor)
        scaled_image = pygame.transform.scale(self.original_image, (new_size, new_size))
        
        self.image = pygame.transform.rotate(scaled_image, tilt_angle)
        self.rect = self.image.get_rect(center=(int(self.player_pos.x), int(self.player_pos.y)))
    
    def drawPlayer(self, screen):
        screen.blit(self.image, self.rect)

    def displayPlayerDATA(self, player_health, player_speed):
        ...