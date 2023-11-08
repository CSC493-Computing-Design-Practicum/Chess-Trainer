from tkinter import *
from tkinter import ttk
from ChessPiece import ChessPiece

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
ttk.Button(frm, text="About").grid(column=1, row=1, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2, ipadx=20, ipady=10, pady=20)

canvas = Canvas(root, width=480, height=480)
canvas.create_rectangle(0, 0, 480, 480, fill="#769656", outline="black")

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
nb1 = ChessPiece("black", "night", (0, 1))
bb1 = ChessPiece("black", "bishop", (0, 2))
qb1 = ChessPiece("black", "queen", (0, 3))
kb1 = ChessPiece("black", "king", (0, 4))
bb2 = ChessPiece("black", "bishop", (0, 5))
nb2 = ChessPiece("black", "night", (0, 6))
rb2 = ChessPiece("black", "rook", (0, 7))

pb1 = ChessPiece("black", "pawn", (1, 0))
pb2 = ChessPiece("black", "pawn", (1, 1))
pb3 = ChessPiece("black", "pawn", (1, 2))
pb4 = ChessPiece("black", "pawn", (1, 3))
pb5 = ChessPiece("black", "pawn", (1, 4))
pb6 = ChessPiece("black", "pawn", (1, 5))
pb7 = ChessPiece("black", "pawn", (1, 6))
pb8 = ChessPiece("black", "pawn", (1, 7))

pw1 = ChessPiece("white", "pawn", (6, 0))
pw2 = ChessPiece("white", "pawn", (6, 1))
pw3 = ChessPiece("white", "pawn", (6, 2))
pw4 = ChessPiece("white", "pawn", (6, 3))
pw5 = ChessPiece("white", "pawn", (6, 4))
pw6 = ChessPiece("white", "pawn", (6, 5))
pw7 = ChessPiece("white", "pawn", (6, 6))
pw8 = ChessPiece("white", "pawn", (6, 7))

rw1 = ChessPiece("white", "rook", (7, 0))
nw1 = ChessPiece("white", "night", (7, 1))
bw1 = ChessPiece("white", "bishop", (7, 2))
qw1 = ChessPiece("white", "queen", (7, 3))
kw1 = ChessPiece("white", "king", (7, 4))
bw2 = ChessPiece("white", "bishop", (7, 5))
nw2 = ChessPiece("white", "night", (7, 6))
rw2 = ChessPiece("white", "rook", (7, 7))

chesspieces = [rb1, nb1, bb1, qb1, kb1, bb2, nb2, rb2, rw1, nw1, bw1, qw1, kw1, bw2, nw2, rw2, pb1, pb2,
               pb3, pb4, pb5, pb6, pb7, pb8, pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8]

for chesspiece in chesspieces:
    if chesspiece.get_color() == "black":
        pos = chesspiece.get_pos()
        piece = chesspiece.get_piece()
        if piece == "rook":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=rb)
        elif piece == "night":
            canvas.create_image(pos[1] * 60 + 30, pos[0] * 60 + 30, image=nb)
        elif piece == "bishop":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=bb)
        elif piece == "queen":
            canvas.create_image(pos[1] * 60 + 30, pos[0] * 60 + 30, image=qb)
        elif piece == "king":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=kb)
        elif piece == "pawn":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=pb)
    elif chesspiece.get_color() == "white":
        pos = chesspiece.get_pos()
        piece = chesspiece.get_piece()
        if piece == "rook":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=rw)
        elif piece == "night":
            canvas.create_image(pos[1] * 60 + 30, pos[0] * 60 + 30, image=nw)
        elif piece == "bishop":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=bw)
        elif piece == "queen":
            canvas.create_image(pos[1] * 60 + 30, pos[0] * 60 + 30, image=qw)
        elif piece == "king":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=kw)
        elif piece == "pawn":
            canvas.create_image(pos[1]*60+30, pos[0]*60+30, image=pw)


canvas.grid(column=2, row=0, pady=20, padx=20)
root.mainloop()
