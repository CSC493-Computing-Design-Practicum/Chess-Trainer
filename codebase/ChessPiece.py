class ChessPiece:
    def __init__(self, color, piece, pos):
        self.color = color
        self.piece = piece
        self.pos = pos

    def __str__(self):
        return f"This is a {self.color} {self.piece} at {self.pos}."

    def get_color(self):
        return self.color

    def get_piece(self):
        return self.piece

    def get_pos(self):
        return self.pos

    def get_chess_pos(self):
        lookup = ["a", "b", "c", "d", "e", "f", "g", "h"]
        return f"{lookup[self.pos[1]]}{8 - self.pos[0]}"

    def move(self, pos):
        self.pos = pos

    # def getAvailableMoves
