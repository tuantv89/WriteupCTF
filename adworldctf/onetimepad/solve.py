from os import urandom
from binascii import unhexlify
P = 0x10000000000000000000000000000000000000000000000000000000000000425


def process(m, k):
    tmp = m ^ k
    res = 0
    for i in bin(tmp)[2:]:
        res = res << 1
        if (int(i)):
            res = res ^ tmp
        if (res >> 256):
            res = res ^ P
    return res


def xprocess(c, a):
    def f(x): return process(a, x)
    pp = c
    p = f(pp)
    while p != c:
        pp = p
        p = f(p)
    return pp


def keygen(seed):
    key = str2num(urandom(32))
    while True:
        yield key
        key = process(key, seed)


def str2num(s):
    return int(s.encode().hex(), 16)


fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"

with open(r"E:\ctf\adworldctf\onetimepad\ciphertext", "r") as f:
    ctxt1, ctxt2, ctxt3 = f.read().splitlines()

c1 = int(ctxt1, 16)
c2 = int(ctxt2, 16)
c3 = int(ctxt3, 16)
key2 = c2 ^ str2num(fake_secret1)
key3 = c3 ^ str2num(fake_secret2)
seed = xprocess(key3, key2)
key1 = xprocess(key2, seed)
flagN = (key1 ^ c1)
flag = hex(flagN)[2:]
print(unhexlify(flag))

