import rsa
import pickle
from bin.encrypt.key_work import *

#load or make key
loadingKeys()





print(bob_pub)
print(bob_priv)
print(crypto)
print(message.decode('utf8'))

#making new key
(pub, priv) = rsa.newkeys(1024)

pickle.dump(pub, open("Keys/pub.dat", "wb"))
pickle.dump(priv, open("Keys/priv.dat", "wb"))

#
filename = input("Save file as: ")


bob_pub = pickle.load(open("Keys/pub.dat", "rb"))
bob_priv = pickle.load(open("Keys/priv.dat", "rb"))

message = 'hello Bob!'.encode('utf8')
crypto = rsa.encrypt(message, bob_pub)


message = rsa.decrypt(crypto, bob_priv)


print(bob_pub)
print(bob_priv)
print(crypto)
print(message.decode('utf8'))

