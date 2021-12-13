
from itertools import cycle


def xor(a, b):
    return [i ^ j for i, j in zip(a, cycle(b))]


r = open(r"E:\ctf\isitdtu\one_time_beach\cipher.enc", "rb").read().strip()
f = r[:20]
cipher = r[20:]

plain = []
plain.append(0xff)
plain.append(0xd8)
plain.append(0xff)
plain.append(0xe0)
plain.append(0x00)
plain.append(0x10)
plain.append(0x4a)
plain.append(0x46)
plain.append(0x49)
plain.append(0x46)
plain.append(0x00)
plain.append(0x01)
plain.append(0x01)
key = []
for i in range(len(plain)):
    key.append(cipher[i] ^ plain[i])
print(key)
key.append(138)
key.append(0x00^cipher[14])
key.append(227)
key.append(177)
key.append(0x01^cipher[17])
key.append(0x00^cipher[18])
key.append(227)
key.append(177)
key.append(227)
key.append(0x00^cipher[22])
key.append(0x43^cipher[23])
key.append(50)
key.append(50)
key.append(168)
print(key)

r = open(r"E:\ctf\isitdtu\one_time_beach\res.jpeg", 'wb')
r.write(bytearray((xor(cipher, key))))
