import base64

#You can get the result by running this python file or read the code learn the result :)
message = "IJ2SAR3JORUHKYRANBSXGYLCYSYW4YJAMFUXIIDNMFUWYIDBMRZGK43JNZUSAYTVNRWWC3WEWEQGC4TEYSYW4ZDBNYQGS3DHNFWGSIDIMVZWC4BANFWGKIDZMFYMJMLMMFXCAR3PN5TWYZJAPFXXE5LNNRQXFRFRN3CLCIDJNZRWK3DFNVSW42JAMJSWW3DJPFXXE5LNFY======"
bytes = message.encode('UTF-8')
message_bytes = base64.b32decode(bytes)
last_message = message_bytes.decode('UTF-8')
print(last_message)