from tkinter import *
from tkinter import ttk

root = Tk()
# root.geometry("800x600")
root.resizable(width=False, height=False)
root["bg"] = "black"

frm = Frame(root)
l1 = ttk.Label(root, text="1", font="15", width=8)
l1.pack()


root.mainloop()