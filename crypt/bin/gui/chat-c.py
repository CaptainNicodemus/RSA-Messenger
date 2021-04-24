#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter.filedialog import askopenfile
from crypt.bin.encrypt import *
import tkinter



def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

# top = tkinter.Tk()
# top.title("Chatter")

# messages_frame = tkinter.Frame(top)
# my_msg = tkinter.StringVar()  # For the messages to be sent.
# my_msg.set("Type your messages here.")
# scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# # Following will contain the messages.
# msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
# messages_frame.pack()

# entry_field = tkinter.Entry(top, textvariable=my_msg)
# entry_field.bind("<Return>", send)
# entry_field.pack()
# send_button = tkinter.Button(top, text="Send", command=send)
# send_button.pack()

# def open_file():
#     file = askopenfile(mode ='r', filetypes =[('Images', '*.jpg')])
#     if file is not None:
#         content = file.read()
#         print(content)
  
# btn = tkinter.Button(top, text ='Open Image', command = lambda:open_file())
# btn.pack(side =tkinter.LEFT)

# top.protocol("WM_DELETE_WINDOW", on_closing)

# top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
# tkinter.mainloop()  # Starts GUI execution.




















# # Python program to implement client side of chat room.
# import socket
# import select
# import sys

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
# 	print ("Correct usage: script, IP address, port number")
# 	exit()
# IP_address = str(sys.argv[1])
# Port = int(sys.argv[2])
# server.connect((IP_address, Port))

# while True:

# 	# maintains a list of possible input streams
# 	sockets_list = [sys.stdin, server]

# 	""" There are two possible input situations. Either the
# 	user wants to give manual input to send to other people,
# 	or the server is sending a message to be printed on the
# 	screen. Select returns from sockets_list, the stream that
# 	is reader for input. So for example, if the server wants
# 	to send a message, then the if condition will hold true
# 	below.If the user wants to send a message, the else
# 	condition will evaluate as true"""
# 	read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

# 	for socks in read_sockets:
# 		if socks == server:
# 			message = socks.recv(2048)
# 			print (message)
# 		else:
# 			message = sys.stdin.readline()
# 			server.send(message)
# 			sys.stdout.write("<You>")
# 			sys.stdout.write(message)
# 			sys.stdout.flush()
# server.close()
