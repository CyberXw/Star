import base64

#You can get the result by running this python file or read the code learn the result :)
message= "LFXXKIDOMVSWIIDUN4QGM2LOMQQHI2DFEBSS23LBNFWCAYLEMRZGK43TEBXWMIDUNBUXGIDBMNRW65LOOQQGC3TEEB2GQZLOEB4W65JANBQXMZJAORXSAZLOORSXEIDUNBSSAZLNMFUWYIDBMRSHEZLTOMQHS33VEBTG65LOMQQGC4ZAMEQGM3DBM4QGS3RAORUGKIDGN5ZG2LRAFBMW65JAMNQW4IDVONSSAYJAMZSWC5DVOJSSA33GEBTWS5DIOVRCA5DPEBTGS3TEEB2GQZJANVQWS3BAMFSGI4TFONZSAORJFE======
bytes = message.encode('ascii')
message_bytes = base64.b32decode(bytes)
last_message = message_bytes.decode('ascii')

print(last_message)