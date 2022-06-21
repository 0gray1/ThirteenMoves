from board import Board, Tile
import pygame

GRAY = (121, 121, 121)
RED = (139, 0, 0)
BLUE = (0, 0, 139)


class Game:
    def __init__(self, board):
        self.board = board

    @classmethod
    def new(cls):
        board = Board.new()
        return cls(board)

    def display(self, surface, x=0, y=0, width=500, height=600, tile_padding=0.07):
        tile_width = width / Board.WIDTH
        tile_height = height / Board.HEIGHT
        tile_filled_width = tile_width * (1 - tile_padding)
        tile_filled_height = tile_height * (1 - tile_padding)

        for board_x in range(Board.WIDTH):
            for board_y in range(Board.HEIGHT):
                tile = self.board.get_tile(board_x, board_y)

                game_x = tile_width*board_x + tile_width*tile_padding/2 + x
                game_y = tile_height*board_y + tile_height*tile_padding/2 + y
                rect = (game_x, game_y, tile_filled_width, tile_filled_height)

                if tile == 0:
                    pygame.draw.rect(surface, GRAY, rect)
                elif not tile.visible:
                    pass
                elif tile.color == Tile.BLUE:
                    pygame.draw.rect(surface, BLUE, rect)
                else:
                    pygame.draw.rect(surface, RED, rect)
