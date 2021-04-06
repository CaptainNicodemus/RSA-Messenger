import rsa



(bob_pub, bob_priv) = rsa.newkeys(4096)
message = 'hello Bob!'.encode('utf8')

crypto = rsa.encrypt(message, bob_pub)

message = rsa.decrypt(crypto, bob_priv)
print(bob_priv)
print(message.decode('utf8'))