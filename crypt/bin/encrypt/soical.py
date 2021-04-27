import pickle
from tkinter.filedialog import askdirectory
from bin.encrypt.encrypt import *
from bin.database_interface.db_interface import *


def send_msg(local_pub):

    print("who are we sending this to?\n"
          "please load folder\n")

    receiver_pubKey = load_recipient_key(which_friend())

    message = input("What is the message? :")

    print("encrypting")
    encrypted_messageR = encryptmsg(receiver_pubKey, message)
    encrypted_messageS = encryptmsg(local_pub, message)
    print("sending")

    send_message(local_pub, encrypted_messageR, encrypted_messageS, receiver_pubKey)
    print("done")
    return




def which_friend():
    path = askdirectory(title='Who are you sending it to?')  # shows dialog box and return the path
    folder_location = path
    return folder_location

def load_recipient_key(folderLocation):

    pub = pickle.load(open(f"{folderLocation}/pub.dat", "rb"))
    return pub


