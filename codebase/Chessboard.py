from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="CHESSTRAINER").grid(row=0, column=0, pady=0)
ttk.Button(frm, text="Start").grid(column=1, row=1, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="About").grid(column=1, row=2, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=3, ipadx=20, ipady=10, pady=20)

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
#

canvas.create_image(30, 30, image=rb)
canvas.create_image(90, 30, image=nb)
canvas.create_image(150, 30, image=bb)
canvas.create_image(210, 30, image=qb)
canvas.create_image(270, 30, image=kb)
canvas.create_image(330, 30, image=bb)
canvas.create_image(390, 30, image=nb)
canvas.create_image(450, 30, image=rb)

canvas.create_image(30, 90, image=pb)
canvas.create_image(90, 90, image=pb)
canvas.create_image(150, 90, image=pb)
canvas.create_image(210, 90, image=pb)
canvas.create_image(270, 90, image=pb)
canvas.create_image(330, 90, image=pb)
canvas.create_image(390, 90, image=pb)
canvas.create_image(450, 90, image=pb)

canvas.create_image(30, 390, image=pw)
canvas.create_image(90, 390, image=pw)
canvas.create_image(150, 390, image=pw)
canvas.create_image(210, 390, image=pw)
canvas.create_image(270, 390, image=pw)
canvas.create_image(330, 390, image=pw)
canvas.create_image(390, 390, image=pw)
canvas.create_image(450, 390, image=pw)

canvas.create_image(30, 450, image=rw)
canvas.create_image(90, 450, image=nw)
canvas.create_image(150, 450, image=bw)
canvas.create_image(210, 450, image=qw)
canvas.create_image(270, 450, image=kw)
canvas.create_image(330, 450, image=bw)
canvas.create_image(390, 450, image=nw)
canvas.create_image(450, 450, image=rw)



canvas.grid(column=2, row=0, pady=20, padx=20)
root.mainloop()

