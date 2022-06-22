import pygame

def alpha_rect(surface, color, alpha=1, rect=None):
    if rect is None:
        x, y, w, h = 0, 0, surface.get_width(), surface.get_height()
    else:
        x, y, w, h = rect

    rect = pygame.Surface((w, h))
    rect.set_alpha(alpha*255)
    rect.fill(color)
    surface.blit(rect, (x, y))
