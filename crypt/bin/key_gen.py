import pickle
import rsa


(pub, priv) = rsa.newkeys(1024)

pickle.dump(pub, open("Keys/pub.dat", "wb"))
pickle.dump(priv, open("Keys/priv.dat", "wb"))

