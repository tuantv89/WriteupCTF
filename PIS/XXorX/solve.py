from Crypto.Util.number import long_to_bytes
from binascii import *

cipher = "1f24203d3f782b242f3b783c2d2461373d78647e616f62781e212034783b2d2c613139367829202a62781b25333a2b2c1b19072800682a121e0b00682a151e0c00682a153c"
cipher = unhexlify(cipher)
plain = "ChristCTF"
for i in range(len(cipher)):
    print("i =", i)
    if i + 8 >= len(cipher):
        break
    key = []
    for j in range(9):
        key.append(cipher[i + j] ^ ord(plain[j]))
    if i == 42:
        print(key)
    flag = b""
    cnt = 0
    for k in range(i, len(cipher)):
        flag += long_to_bytes(cipher[k] ^ key[cnt % len(key)])
        cnt += 1
    print(flag)
key = [88, 77, 65, 83, 88, 88]
flag = b""
for i in range(len(cipher)):
    flag += long_to_bytes(cipher[i] ^ key[i % len(key)])
print(flag)
# ChristCTF{X0r__XX0rX__X0rX}
