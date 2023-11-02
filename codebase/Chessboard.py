from tkinter import *
from tkinter import ttk

root = Tk()


frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="CHESSTRAINER").grid(row=0, column=0, pady=0)
ttk.Button(frm, text="Start").grid(column=1, row=1, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="About").grid(column=1, row=2, ipadx=20, ipady=10, pady=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=3, ipadx=20, ipady=10, pady=20)

canvas = Canvas(root, width=400, height=400)
canvas.create_rectangle(0, 0, 400, 400, fill="black")
canvas.grid(column=2, row=0)
root.mainloop()