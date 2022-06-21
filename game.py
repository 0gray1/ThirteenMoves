from board import Board, Tile
import pygame

GRAY = (121, 121, 121)
RED = (139, 0, 0)
BLUE = (0, 0, 139)


class Game:
    def __init__(self, board, x, y, width, height, tile_padding):
        self.board = board
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tile_padding = tile_padding

        self.tile_width = self.width / Board.WIDTH
        self.tile_height = self.height / Board.HEIGHT
        self.tile_filled_width = self.tile_width * (1 - self.tile_padding)
        self.tile_filled_height = self.tile_height * (1 - self.tile_padding)

        self.held_tile = None
        self.player = Tile.BLUE

    @classmethod
    def new(cls, x=0, y=0, width=500, height=600, tile_padding=0.07):
        board = Board.new()
        return cls(board, x, y, width, height, tile_padding)

    def switch_player(self):
        if self.player == Tile.BLUE:
            self.player = Tile.RED
        else:
            self.player = Tile.BLUE

    def display(self, surface, events):
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                self.display_tile(surface, x, y)

        if not (self.held_tile is None):
            self.display_tile_on_mouse(surface, self.held_tile, events.mouse_pos)

    def display_tile(self, surface, x, y):
        tile = self.board.get_tile(x, y)

        game_x = self.tile_width * x + self.tile_width * self.tile_padding / 2 + self.x
        game_y = self.tile_height * y + self.tile_height * self.tile_padding / 2 + self.y
        rect = (game_x, game_y, self.tile_filled_width, self.tile_filled_height)

        if tile == 0 or not tile.visible:
            pygame.draw.rect(surface, GRAY, rect)
        elif tile.color == Tile.BLUE:
            pygame.draw.rect(surface, BLUE, rect)
        else:
            pygame.draw.rect(surface, RED, rect)

    def mouse_pos_to_tile(self, mouse_pos):
        tile_width = self.width / Board.WIDTH
        tile_height = self.height / Board.HEIGHT

        x, y = mouse_pos
        x = (x - self.x) / tile_width
        y = (y - self.y) / tile_height

        return round(x-0.5), round(y-0.5)

    def update(self, events):
        mouse_down, mouse_up = events.mouse_down, events.mouse_up
        if not mouse_down and not mouse_up:
            return

        mouse_pos = events.mouse_pos
        x, y = self.mouse_pos_to_tile(mouse_pos)

        if mouse_down and Board.in_bounds(x, y):
            self.select_tile(x, y)
        elif mouse_up and not (self.held_tile is None):
            self.release_tile(x, y)

    def display_tile_on_mouse(self, surface, tile, mouse_pos):
        x, y = mouse_pos
        w, h = self.tile_filled_width, self.tile_filled_height
        rect = (x - w/2, y - h/2, w, h)

        if tile.color == Tile.BLUE:
            pygame.draw.rect(surface, BLUE, rect)
        else:
            pygame.draw.rect(surface, RED, rect)

    def select_tile(self, x, y):
        tile = self.board.get_tile(x, y)
        if tile == 0:
            return
        if tile.color != self.player:
            return
        self.held_tile = tile
        self.held_tile.visible = False

    def release_tile(self, x, y):
        move = self.held_tile.get_move(x, y)
        if self.held_tile.is_valid_move(self.board, move):
            self.board.perform_move(move)
            self.switch_player()
        self.held_tile.visible = True
        self.held_tile = None
