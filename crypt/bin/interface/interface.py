from tkinter import filedialog, Tk

root = Tk().withdraw()

file = filedialog.asksaveasfile(mode='w', defaultextension=".dat")

