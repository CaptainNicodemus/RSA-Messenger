import pickle
from asyncore import loop

import rsa

def loadingKeys():
    action = input("load or make new keys? (l/n)")
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

    pickle.dump(pub, open("Keys/pub.dat", "wb"))
    pickle.dump(priv, open("Keys/priv.dat", "wb"))

    print('\nmaking new keys...\n')
    (pub, priv) = rsa.newkeys(1024)

    pickle.dump(pub, open("Keys/pub.dat", "wb"))
    pickle.dump(priv, open("Keys/priv.dat", "wb"))
    print('keys made and saved\n\n')

def loadkeys():
    pass

def userNameUpdate():

    while loop:

        userName= input("Enter new public user name: ")
        userName = userName.strip()

        #check number

        numb = '#1234'

        print("Is this ok? :", userName,numb)
        action = input("Is this ok : ?")

        if player_action == '1':
            act1

        elif player_action == '2':
            act2
            return

        else:
            print("Please type \'1\', \'2\', \'3\', or \'4\'")

    return userName
