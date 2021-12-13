from pwn import *
conn = remote('168.119.108.148', 13010)

for i in range(4):
    conn.recvline()

while True:
    inputs = []
    for i in range(7):
        s = conn.recvline()
        print(s)
        inputs.append(s)
    p = int(inputs[2].split()[-1])
    n = int(inputs[5].split()[-1])
    deg = int(inputs[6].split()[-1][:-1])
    a = p + 1 - n
    val = [2, a]
    for i in range(2, deg + 1):
        val.append(a * val[i-1] - p * val[i-2])
    ans = (p ** deg) + 1 - val[deg]
    conn.sendline(str(ans))
    print(conn.recvline())
