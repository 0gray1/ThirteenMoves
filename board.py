from tile import Tile


class Board:
    WIDTH = 5
    HEIGHT = 6

    def __init__(self, tiles):
        self.tiles = tiles

    def __str__(self):
        """
        Accessing via class name, instead of `self`, is slightly
        faster; ie Board.HEIGHT as opposed to self.HEIGHT
        """
        string = "------------------\n"
        for y in range(Board.HEIGHT):
            string += "| "
            for x in range(Board.WIDTH):
                tile = self.tiles[x][y]
                if tile != 0:
                    string += str(tile)
                    string += "  "
                else:
                    string += ".. "
            string += "| \n"
        string += "------------------"
        return string + "\n"

    @classmethod
    def clone(cls):
        tiles = [[0 for _ in range(Board.HEIGHT)] for _ in range(Board.WIDTH)]

        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                tile = Board.tiles[x][y]
                if tile != 0:
                    tiles[x][y] = tile.clone()

        return cls(tiles)

    @classmethod
    def new(cls):
        tiles = [[0 for _ in range(Board.HEIGHT)] for _ in range(Board.WIDTH)]

        for x in range(Board.WIDTH):
            tiles[x][0] = Tile(x, 0, Tile.RED)
            tiles[x][Board.HEIGHT-1] = Tile(x, Board.HEIGHT-1, Tile.BLUE)

        return cls(tiles)

    @staticmethod
    def in_bounds(x, y):
        return 0 <= x < Board.WIDTH and 0 <= y < Board.HEIGHT

    def get_tile(self, x, y):
        return self.tiles[x][y]

    def perform_move(self, move):
        tile = self.tiles[move.xfrom][move.yfrom]
        tile.x = move.xto
        tile.y = move.yto
        self.tiles[move.xto][move.yto] = tile
        self.tiles[move.xfrom][move.yfrom] = 0

    def is_winning(self, color):
        if color == Tile.BLUE:
            end_row = 0
            other = Tile.RED
        else:
            end_row = Board.HEIGHT - 1
            other = Tile.BLUE

        for x in range(Board.WIDTH):
            tile = self.get_tile(x, end_row)
            if tile == 0:
                continue
            if tile.color == color:
                return True

        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                tile = self.get_tile(x, y)
                if tile == 0:
                    continue
                if tile.color == other:
                    return False

        return True
