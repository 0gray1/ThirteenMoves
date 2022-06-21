from events import Events
from game import Game
import pygame

WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode([600, 700])

    game = Game.new(50, 50)

    running = True
    while running:
        events = Events.update()

        if events.quit:
            running = False

        screen.fill(WHITE)
        game.update(events)
        game.display(screen, events)
        pygame.display.flip()


if __name__ == "__main__":
    main()
