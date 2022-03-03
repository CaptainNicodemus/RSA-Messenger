from tkinter.filedialog import askopenfile
from chat-c import *
import tkinter

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Images', '*.jpg')])
    if file is not None:
        content = file.read()
        print(content)
  
btn = tkinter.Button(top, text ='Open Image', command = lambda:open_file())
btn.pack(side =tkinter.LEFT)

top.protocol("WM_DELETE_WINDOW", on_closing)

top.protocol("WM_DELETE_WINDOW", on_closing)

tkinter.mainloop()  # Starts GUI execution.