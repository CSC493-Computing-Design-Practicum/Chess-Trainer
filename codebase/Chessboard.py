from tkinter import *
from tkinter import ttk
from ChessPiece import ChessPiece


def about():
    """
    This is just the function that will be used for the about button
    :return: NONE
    """
    print("You should see some cool info now! Do you?")


def get_event(event):
    pos = calculate_pos(event)
    id = find_piece(pos[0], pos[1])
    moves = id.raw_moves()


def calculate_pos(event):
    """
    This just goes from pixel position to chess position.
    :param event: The click we are finding the position of
    :return: the position
    """
    x = event.x // 60
    y = event.y // 60
    return x, y


def find_piece(x, y):
    """
    Tells us if there is a piece in the position (x, y) or not.
    :param x: the x coordinate of the position
    :param y: the y coordinate of the position
    :return: the piece if one is found
    """
    for i in chesspieces:
        if i.get_pos() == (x, y):
            return i

# This is the board, it has -1 on the sides to represent out of bounds, this idea comes from professor Deanna Wilborne
board = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, "rb", "nb", "bb", "qb", "kb", "bb", "nb", "rb", -1, -1],
         [-1, -1, "pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb", -1, -1],
         [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
         [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
         [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
         [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1],
         [-1, -1, "pw", "pw", "pw", "pw", "pw", "pw", "pw", "pw", -1, -1],
         [-1, -1, "rw", "nw", "bw", "qw", "kw", "bw", "nw", "rw", -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

root = Tk()

root.title("CHESSTRAINER")

logo = PhotoImage(file="chess_logo.png")
root.iconphoto(False, logo)

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Start").grid(column=1, row=0, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="About", command=about).grid(column=1, row=1, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2, ipadx=20, ipady=10, pady=20)

canvas = Canvas(root, width=480, height=480)
canvas.create_rectangle(0, 0, 480, 480, fill="#769656", outline="black")
canvas.bind("<Button-1>", get_event)

# bb = PhotoImage(file="ChessPieces/bb.png")
pieces = ["bb", "bw", "kb", "kw", "nb", "nw", "pb", "pw", "qb", "qw", "rb", "rw"]

for i in pieces:
    globals()[i] = PhotoImage(file=f"ChessPieces/{i}.png")

for i in range(0, 12):
    for r in range(0, 12):
        sum = i + r
        if board[i][r] != -1 and sum % 2 == 0:
            canvas.create_rectangle((i-2)*60, (r-2)*60, (i-2)*60+60, (r-2)*60+60, fill="#eeeed2")

rb1 = ChessPiece("black", "rook", (0, 0))
nb1 = ChessPiece("black", "night", (1, 0))
bb1 = ChessPiece("black", "bishop", (2, 0))
qb1 = ChessPiece("black", "queen", (3, 0))
kb1 = ChessPiece("black", "king", (4, 0))
bb2 = ChessPiece("black", "bishop", (5, 0))
nb2 = ChessPiece("black", "night", (6, 0))
rb2 = ChessPiece("black", "rook", (7, 0))

pb1 = ChessPiece("black", "pawn", (0, 1))
pb2 = ChessPiece("black", "pawn", (1, 1))
pb3 = ChessPiece("black", "pawn", (2, 1))
pb4 = ChessPiece("black", "pawn", (3, 1))
pb5 = ChessPiece("black", "pawn", (4, 1))
pb6 = ChessPiece("black", "pawn", (5, 1))
pb7 = ChessPiece("black", "pawn", (6, 1))
pb8 = ChessPiece("black", "pawn", (7, 1))

pw1 = ChessPiece("white", "pawn", (0, 6))
pw2 = ChessPiece("white", "pawn", (1, 6))
pw3 = ChessPiece("white", "pawn", (2, 6))
pw4 = ChessPiece("white", "pawn", (3, 6))
pw5 = ChessPiece("white", "pawn", (4, 6))
pw6 = ChessPiece("white", "pawn", (5, 6))
pw7 = ChessPiece("white", "pawn", (6, 6))
pw8 = ChessPiece("white", "pawn", (7, 6))

rw1 = ChessPiece("white", "rook",   (0, 7))
nw1 = ChessPiece("white", "night",  (1, 7))
bw1 = ChessPiece("white", "bishop", (2, 7))
qw1 = ChessPiece("white", "queen",  (3, 7))
kw1 = ChessPiece("white", "king",   (4, 7))
bw2 = ChessPiece("white", "bishop", (5, 7))
nw2 = ChessPiece("white", "night",  (6, 7))
rw2 = ChessPiece("white", "rook",   (7, 7))

chesspieces = [rb1, nb1, bb1, qb1, kb1, bb2, nb2, rb2, rw1, nw1, bw1, qw1, kw1, bw2, nw2, rw2, pb1, pb2,
               pb3, pb4, pb5, pb6, pb7, pb8, pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8]

for chesspiece in chesspieces:
    if chesspiece.get_color() == "black":
        pos = chesspiece.get_pos()
        piece = chesspiece.get_piece()
        if piece == "rook":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=rb)
        elif piece == "night":
            canvas.create_image(pos[0] * 60 + 30, pos[1] * 60 + 30, image=nb)
        elif piece == "bishop":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=bb)
        elif piece == "queen":
            canvas.create_image(pos[0] * 60 + 30, pos[1] * 60 + 30, image=qb)
        elif piece == "king":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=kb)
        elif piece == "pawn":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=pb)
    elif chesspiece.get_color() == "white":
        pos = chesspiece.get_pos()
        piece = chesspiece.get_piece()
        if piece == "rook":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=rw)
        elif piece == "night":
            canvas.create_image(pos[0] * 60 + 30, pos[1] * 60 + 30, image=nw)
        elif piece == "bishop":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=bw)
        elif piece == "queen":
            canvas.create_image(pos[0] * 60 + 30, pos[1] * 60 + 30, image=qw)
        elif piece == "king":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=kw)
        elif piece == "pawn":
            canvas.create_image(pos[0]*60+30, pos[1]*60+30, image=pw)

canvas.grid(column=2, row=0, pady=20, padx=20)
root.mainloop()

