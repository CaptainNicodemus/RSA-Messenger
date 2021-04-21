import pickle
import os
import rsa
from asyncore import loop
from bin.database_interface.db_interface import *

def loadingKeys():
    action = input("load or make new user? (l/n)")
    if action == 'l':
        return loadkeys()
    elif action == 'n':
        return newkeys()
    else:
        print("error")


def newkeys():
    pub = None
    priv = None

    userName = userNameUpdate()

    print('\nCreating a new file')
    createFolder(f"keys/{userName}")
    folder1 = f"keys/{userName}/pub.dat"
    folder2 = f"keys/{userName}/priv.dat"

    pickle.dump(pub, open(folder1, "wb"))
    pickle.dump(priv, open(folder2, "wb"))

    print('\nmaking new keys...\n')
    (pub, priv) = rsa.newkeys(1024)

    pickle.dump(pub, open(f"keys/{userName}/pub.dat", "wb"))
    pickle.dump(priv, open(f"keys/{userName}/priv.dat", "wb"))
    print('keys made and saved\n\n')

    folder_location = f"keys/{userName}"

    add_user(userName,pub)



    return loadkeys(folder_location)


def loadkeys(folderLocation):
    #give folder with key's (pub.dat) & (priv.dat) retuns values

    user_name = folderLocation
    pub = pickle.load(open(f"{folderLocation}/pub.dat", "rb"))
    priv = pickle.load(open(f"{folderLocation}/priv.dat", "rb"))

    return pub, priv, user_name



def userNameUpdate():
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
