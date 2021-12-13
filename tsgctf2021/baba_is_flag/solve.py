# import ecdsa
# from sympy import *
# par = ecdsa.SECP256k1
# curve = par.curve
# G = par.generator
# print(G.x(), end=" ")
# print(G.y())
# n = par.order
# print(n)
# P=curve.p()
# print(P)
# x = 28204895145442690566688798772404083895941637723751236952072199061697425781603
# s = 20401767886725555310052173458579234019357203737433903414525742198435240000191
# tmp=(5*G).x()
# print(tmp)
# print(pow(5,G.x(),P))


#sage
from pwn import *
from Crypto.Util.number import bytes_to_long,isPrime
r = remote('34.146.212.53', 65434)

p = (1 << 256) - (1 << 32) - (1 << 9) - \
    (1 << 8) - (1 << 7) - (1 << 6) - (1 << 4) - 1

E = EllipticCurve(GF(p), [0, 7])
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

G = E(Gx, Gy)
n = E.order()
print(isPrime(n))

h1 = bytes_to_long(hashlib.sha256(b'Baba').digest())
h2 = bytes_to_long(hashlib.sha256(b'Flag').digest())

for i in range(3):
    r.recvline()
r.sendline(b"1")
r.recvline()
X1 = int(r.recvline().split()[-1])
S1 = int(r.recvline().split()[-1])

print(X1)
print(S1)


target1 = S1 * E.lift_x(GF(p)(X1))

target2 = target1 + (h2 - h1) * G
for i in range(3):
    r.recvline()
r.sendline(b"2")
r.sendline("Flag")
r.sendline(str(int(target2.xy()[0])))
r.sendline(b"1")
print(r.recvline())
print(r.recvline())
