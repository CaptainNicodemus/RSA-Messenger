import pickle
import os
import rsa
from asyncore import loop


def load_recipient_key(folderLocation):

    user_name = folderLocation
    pub = pickle.load(open(f"{folderLocation}/pub.dat", "rb"))
    return pub, user_name
