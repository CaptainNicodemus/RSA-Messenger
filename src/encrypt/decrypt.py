import rsa

def decryptmsg(privatekey,msg):
    # recevered priv key and msg, return decrypted msg

    msg = rsa.decrypt(msg, privatekey)
    msg = msg.decode('utf8')

    return msg


# priv = rsa.PrivateKey(121574974811024066625968958728159748546388703699372955557776668504297051439308738442978908836488818751760615050214414171470108516531550296428790778318176528117533716142074996016050205430046775048434001781897647313914814621256207801188084334106984548597846128992109356022704886489846722381844302415701888711671, 65537, 66258982716635757079914540913566533386940380529078279851269771970588859473415467899145836181419772467085549359347520414064869249332040122188131091298975975252490922375405055425516089169447115187322563670414332332066021480329677883967006654835443735855869622541558907399607885546501580393158870854078988110289, 47301294606113992149662422681946933473325061666491234904560135756981965103986123468611066607254814887278606026712103365052952866045298146186030786343046582788894589, 2570225103211228610264510961403619421560528223887954782314499834226754387232773521870563348409203371490643384336598468158440020025577647722814339)
# mssg = bytes(b"aIz\x1b\x18\xe9\xd5\x7f5\x9e\x93\x0c\x0e\xeajhZ1H\x1c\xdd\xe6N(\x14\xe6\x82-_\xc6\x1d\xdd\xf8\x80\xc2\x0f\xbd\xb0]o\xcc]\xba\xb7c\xac\x9f\xa0\xa0\xe8\x14\xf2\xd6qd\x9b\x9fE\xd3\xe5\xa9o\xc3\xa6\x0c\xa0*\xb9\xb7H\xea&\x8173\x1e\xd4\x93\xc1\xd6)\xc4\x00%\xc7\xd5|dnc\x0c\xe5J\xbcd\x8eP\x02%\xcf-\xc2'>Y\x1e\xea\x9d\x9dY\x8d\xaa&\xa8\x0b\xd9\xe5\xd4\xa5\x97\xbf\x1f\x8e\xf4\xafFZ4")
#
# print(decryptmsg(priv,mssg))