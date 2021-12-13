from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

flag = b"???"
flag = pad(flag, AES.block_size)

p = random_prime(2^120)
M = Matrix(GF(p),8,8)
M.randomize()
a = randint(0,p)
b = randint(0,p)
S = M^(a*b)

print(p)
print(list(M))
print(list(M^a))
print(list(M^b))

key = sha256(S.str().encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(flag)
print(enc.hex())
