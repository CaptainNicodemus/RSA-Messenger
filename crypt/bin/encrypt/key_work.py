import pickle
import os
from asyncore import loop
import rsa


def loadingKeys():
    action = input("load or make new user? (l/n)")
    if action == 'l':
        loadkeys()
    elif action == 'n':
        newkeys()
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

    pickle.dump(pub, open("Keys/pub.dat", "wb"))
    pickle.dump(priv, open("Keys/priv.dat", "wb"))
    print('keys made and saved\n\n')


def loadkeys():

    #User picks folder with key's (pub.dat) & (priv.dat)


    pass


def userNameUpdate():
    while loop:

        userName = input("Enter new public user name: ")
        userName = userName.strip()

        # check number
        numb = '#1234'

        print("Is this ok? :", userName, numb)
        action = input("y/n :")

        if action == 'y':
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
