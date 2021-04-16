import rsa

def encryptmsg(publickey,msg):
    #recevered public key and msg, return encrypted msg

    msg = msg.encode('utf8')
    msg = rsa.encrypt(msg,publickey)

    return msg