from pwn import *
r = remote("ctf.k3rn3l4rmy.com",2234)
#r.interactive()
k=2
n=0
for i in range(600):
    print("[+] Try",i+1)
    r.sendline(str(k).encode())
    l=(1<<i)-n
   # print(": send l =", l, end="")
    #print(" k =", k, end=" ")
    r.sendline(str(l).encode())
    r.recvuntil(b"= ")
    res=r.recvline().strip()
   # print(" receive =",res.decode())
    if(int(res)==k):
        n+=(1<<i)
    k*=2
r.sendline(str(n).encode())
r.interactive()
#flag{h4cking_th3_GCD!}
