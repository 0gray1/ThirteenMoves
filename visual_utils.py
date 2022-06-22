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


def centered_text(surface, text, x=0, y=0, color=(0, 0, 0), font_size=60, font="arialblack"):
    font = pygame.freetype.SysFont(font, font_size)
    text_rect = font.get_rect(text)
    text_rect.center = x, y
    font.render_to(surface, text_rect.topleft, text, color)
