from pwn import *
from binascii import *
from Crypto.Util.number import *

r = remote("flipmeover.chall.cryptonite.team", 1337)
sendstr = b"a" * 39 + b"gimmeflaa"
r.recvuntil(b"Enter username in hex():\n")
r.sendline(sendstr.hex().encode())
token = r.recvline().strip()
tag = token[:32]
cipher = token[32:]
blocks = []
for i in range(32, len(token), 32):
    blocks.append(list(unhexlify(token[i : i + 32])))
for i in range(0, 256):
    print("[+] Try i =",i)
    blocks[1][15] = i
    r.recvuntil(b"Enter token in hex():\n")
    new_token = b""
    for j in range(len(blocks)):
        for k in range(len(blocks[j])):
            new_token += long_to_bytes(blocks[j][k])
    new_token = tag + new_token.hex().encode()
    r.sendline(new_token)
    r.recvuntil(b"Enter tag in hex():\n")
    r.sendline(tag)
    tmp = r.recvline().strip().decode()
    if tmp == "Oh no u flipped me...":
        r.interactive()
    r.recvuntil(b"Is your username ")
    x = r.recvline().strip()
    x = unhexlify(x)
    print(x)
    print()

# nite{flippity_floppity_congrats_you're_a_nerd}
