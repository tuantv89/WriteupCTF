import re
from pwn import *

r = remote('95.217.210.96', 11010)

def gcd(u, v):
    while v:
        u, v = v, u % v
    return u

def rvlines(lines):
    return [r.recvline().decode().strip() for _ in range(lines)]

rvlines(10)

r.sendline(b'P')
r.sendline(b'T')
r.sendline(b'1')
r.sendline(b'T')
r.sendline(b'2')
pub = int(rvlines(2)[0].split(' = ')[1])
c1 = int(rvlines(2)[0].split(': ')[1])
c2 = int(rvlines(1)[0].split(': ')[1])

F.<x> = PolynomialRing(Zmod(pub))
f1 = (x + 1) ** 5 + (x + 1) - c1
f2 = (x + 2) ** 5 + (x + 2) - c2
g = gcd(f1, f2) # ax + b
b, a = g.coefficients()
print(re.findall(r'ASIS{.+}', bytes.fromhex(hex(-b / a)[2:]).decode())[0])