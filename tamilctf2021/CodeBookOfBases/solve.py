import base64
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
f = open("E:\ctf\\tamilctf2021\CodeBookOfBases\key", 'rb').read().strip()
key = base64.b64encode(f)
key = int(key.decode(), 2)
key = long_to_bytes(key)
print(key.decode())
decode = AES.new(key, AES.MODE_ECB)
ct = "oPgiWmZzdeMhyA80iS9c6la2TlIuIJ1HFRAEvH+8zgo="
ct = base64.b64decode(ct)
pt = decode.decrypt(ct)
print(pt.decode())
