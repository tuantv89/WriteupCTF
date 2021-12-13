from pwn import *
r = remote("125.235.240.166",20123)
r.recvuntil(b"#1:\n")
r.recvline()
r.recvline()
x=r.recvuntil(b"Number:")
print(x)
r.close()
