import rsa

def decryptmsg(privatekey,msg):
    # recevered priv key and msg, return decrypted msg

    msg = rsa.decrypt(msg, privatekey)
    msg = msg.decode('utf8')

    return msg

