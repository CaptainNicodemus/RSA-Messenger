import pickle
import os
import rsa
import time
from asyncore import loop
from bin.database_interface.db_interface import *
from tkinter.filedialog import askdirectory


def loadingKeys():
    action = input("load or make new user? (l/n)")
    if action == 'l':
        return loadkeys(ask_4_which_keys())
    elif action == 'n':
        return newkeys()
    else:
        print("error")


def newkeys():
    pub = None
    priv = None

    user_name = ask_4_new_username()

    print('\ncreating a new file')
    createFolder(f"keys/myKeys/{user_name}")
    folder1 = f"keys/myKeys/{user_name}/pub.dat"
    folder2 = f"keys/myKeys/{user_name}/priv.dat"

    pickle.dump(pub, open(folder1, "wb"))
    pickle.dump(priv, open(folder2, "wb"))

    print('making new keys...')
    (pub, priv) = rsa.newkeys(1024)

    pickle.dump(pub, open(f"keys/myKeys/{user_name}/pub.dat", "wb"))
    pickle.dump(priv, open(f"keys/myKeys/{user_name}/priv.dat", "wb"))
    print('keys made and saved')

    folder_location = f"keys/myKeys/{user_name}"

    print('Updateing Database with new user')
    #adds user to database
    user_name_update(pub, user_name)
    print('\nLocked and loaded\n\n')

    return loadkeys(folder_location)

def ask_4_which_keys():
    path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    folder_location = path
    return folder_location

def loadkeys(folderLocation):
    # give folder with key's (pub.dat) & (priv.dat) retuns values

    user_name = folderLocation
    pub = pickle.load(open(f"{folderLocation}/pub.dat", "rb"))
    priv = pickle.load(open(f"{folderLocation}/priv.dat", "rb"))

    return pub, priv, user_name


def ask_4_new_username():
    while loop:

        userName = input("Enter new public user name: ")
        userName = userName.strip()

        print("Is this ok? :", userName)
        action = input("y/n :")

        if action == 'y':
            userName = userName
            return userName

        elif action == 'n':
            print("lets try again")

        else:
            print("error")
            return


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def run_rsa_algo_primes():
    print("V0.3.13b")
    print("loading RSA algo.")
    time.sleep(.3)
    print("done\n\n\n\n")
    return


