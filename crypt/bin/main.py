from bin.encrypt.key_work import *
from bin.encrypt.soical import *


#bootup
#run_rsa_algo_primes()
#load or make key
local_pub,local_priv,my_userName = loadingKeys()

#loading friends public keys
friends_key_table = [0, 0]
#update usernames

#pull messages

#de-code messages

while loop:

    action = input("\nWhat would you like to do?\n"
                   "\n1 - send message"
                   "\n2 - load messages"
                   "\n3 - ReLoad user keys"
                   "\n4 - Display keys"
                   "\n5 - update my username"
                   "\n6 - exit"
                   "\n:")

    if action == '1':
        send_msg(local_pub)

    elif action == '2':
        print("lets try again")

    elif action == '3':
        local_pub,local_priv,my_userName = loadingKeys()

    elif action == '4':
        print("\n*WARNING SHARING PRIVATE KEYS ARE A SECURITY RISK*")
        action = input("Do you still want to continue? (y/n)\n")
        if action == 'y':
            print(my_userName)
            print(local_pub)
            print(local_priv)

        elif action == 'n':
            print("")

    elif action == '5':
        user_name = ask_4_new_username()
        user_name_update(local_pub, user_name)
        #add change file name

    elif action == '6':
        print("good bye")
        exit()
    else:
        print("error")
        exit()

