import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
mKey = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
greeting.pack()

window.mainloop()