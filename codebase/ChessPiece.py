class ChessPiece:
    def __init__(self, color, piece, pos):
        self.color = color
        self.piece = piece
        self.pos = pos

    def __str__(self):
        return f"This is a {self.color} {self.piece} at {self.pos}."

    def get_color(self):
        """
        Simple get function for color.
        :return: the color
        """
        return self.color

    def get_piece(self):
        """
        Simple get function for piece.
        :return: the type of piece it is ex. bishop
        """
        return self.piece

    def get_pos(self):
        """
        Simple get function for position
        :return: the position of the piece
        """
        return self.pos

    def get_chess_pos(self):
        """
        Tells you what the position of the piece is in terms of a chess board.
        :return: the chess board position of the piece
        """
        lookup = ["a", "b", "c", "d", "e", "f", "g", "h"]
        return f"{lookup[self.pos[1]]}{8 - self.pos[0]}"

    def move(self, pos):
        """
        Moves the piece to the position
        :param pos: the postion to move the piece to.
        :return: None
        """
        self.pos = pos
