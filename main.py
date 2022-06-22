from events import Events
from game import Game
import pygame

WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode([600, 800])
    pygame.display.set_caption("Thirteen Moves")

    game = Game.new(50, 150)

    running = True
    while running:
        events = Events.update()

        if events.quit:
            running = False

        screen.fill(WHITE)
        game.update(events)
        game.display(screen, events)
        game.display_move_counter(screen, 300, 75)
        pygame.display.flip()


if __name__ == "__main__":
    main()
