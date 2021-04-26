from bin.database_interface.db_interface import *
from bin.encrypt.key_work import *
from bin.encrypt.encrypt import *
from bin.encrypt.decrypt import *

#bootup
run_rsa_algo_primes()
#load or make key
local_pub,local_priv,my_userName = loadingKeys()

#loading friends public keys
friends_key_table = [0, 0]
#update usernames

#pull messages

#de-code messages


# display msg

#send messages

message = "This is a test"
message = encryptmsg(local_pub,message)


send_message(local_pub,message,message,local_pub)




#this is trash right now


print(local_pub)
print(local_priv)
print(my_userName)


