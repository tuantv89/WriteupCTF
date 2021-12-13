from Crypto.Util.number import long_to_bytes,bytes_to_long
from base64 import *
l = open(r"E:\ctf\adworldctf\enc\output.txt", "r").read().strip().split()
f=""
for s in l:
    if s=="ZERO":
        f+="0"
    else:
        f+="1"
f=int(f,2)
f=long_to_bytes(f).decode()
print(b64decode(f))
