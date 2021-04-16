import rsa
import pickle
from bin.encrypt.key_work import *

#load or make key
loadingKeys()


#pull messages useing public key



#send messages





#this is trash right now


print(bob_pub)
print(bob_priv)
print(crypto)
print(message.decode('utf8'))

#making new key
(pub, priv) = rsa.newkeys(1024)



message = 'hello Bob!'.encode('utf8')
crypto = rsa.encrypt(message, bob_pub)


message = rsa.decrypt(crypto, bob_priv)


print(bob_pub)
print(bob_priv)
print(crypto)
print(message.decode('utf8'))