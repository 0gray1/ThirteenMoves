from move import Move


class Tile:
    RED = "R"
    BLUE = "B"

    def __init__(self, x, y, color, visible=True):
        self.x = x
        self.y = y
        self.color = color
        self.visible = visible

        # Y direction the tile can move in
        if color == self.BLUE:
            self.direction = -1
        else:
            self.direction = 1

    def __str__(self):
        return str(self.color)

    def clone(self):
        return Tile(self.x, self.y, self.color, self.visible)

    def get_move(self, xto, yto):
        return Move(self.x, self.y, xto, yto)

    def is_valid_move(self, board, move):
        xto, yto = move.xto, move.yto

        if not board.in_bounds(xto, yto):
            return False
        if not yto - self.y == self.direction:
            return False

        # A tile cannot be moved onto another tile of the same color
        to_tile = board.get_tile(xto, yto)
        if to_tile == 0:
            return True
        if self.color == to_tile.color:
            return False

        return True

    def get_valid_moves(self, board):
        x, y, direction = self.x, self.y, self.direction

        possible_moves = [
            self.get_move(x - 1, y + direction),
            self.get_move(x, y + direction),
            self.get_move(x + 1, y + direction)
        ]

        valid_moves = []
        for move in possible_moves:
            if self.is_valid_move(board, move):
                valid_moves.append(move)

        return valid_moves
