import rsa



(bob_pub, bob_priv) = rsa.newkeys(1024)

message = 'hello Bob!'.encode('utf8')
crypto = rsa.encrypt(message, bob_pub)


message = rsa.decrypt(crypto, bob_priv)


print(bob_pub)
print(bob_priv)
print(crypto)
print(message.decode('utf8'))