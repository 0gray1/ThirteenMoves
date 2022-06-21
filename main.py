from game import Game
import pygame

WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode([600, 700])

    game = Game.new()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        game.display(screen, 50, 50)
        pygame.display.flip()


if __name__ == "__main__":
    main()
