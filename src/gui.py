import pygame

def render_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def render_GUI_Box(screen, size, name, color, position):
    x, y = position
    w, h = size

    box_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, box_rect)
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 3)

    font_size = max(16, int(h * 0.45))
    font = pygame.font.SysFont("Arial", font_size, bold=True)
    text = font.render(name, True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=box_rect.center))

    return box_rect
