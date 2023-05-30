from tkinter import *
from tkinter.ttk import *

master = Tk()

L1 = Label(master, text = "First Name")
L2 = Label(master, text = "Middle Name")
L3 = Label(master, text = "Last Name")

L1.grid(row = 0, column = 0, sticky = W, pady = 10, padx = 5)
L2.grid(row = 1, column = 0, sticky = W, pady = 10, padx = 5)
L3.grid(row = 2, column = 0, sticky = W, pady = 10, padx = 5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row = 0, column = 1, pady = 10, padx = 5)
e2.grid(row = 1, column = 1, pady = 10, padx = 5)
e3.grid(row = 2, column = 1, pady = 10, padx = 5)

mainloop()
