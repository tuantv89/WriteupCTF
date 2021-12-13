from Crypto.Util.number import *

enc = open("E:\ctf\\asis2021\Warmup\output.txt", "r").read().strip()
enc = enc[6:]
p = len(enc)
print(p)
message = ['?']*p
res = []
for possible_s in range(1, p):
    message = ['?']*p
    message[0] = 'A'
    message[1] = 'S'
    print("[+]Testing with s =", possible_s)
    for i in range(1, p-1):
        mod = pow(possible_s, i, p)
        message[mod] = enc[i+1]
    flag = "".join(message)
    if("ASIS{" in flag):
        print(flag[:100])
        res.append(flag[:100])
for i in res:
    print(i)
# ASIS{_how_d3CrYpt_Th1S_h0m3_m4dE_anD_wEird_CrYp70_5yST3M?!!!!!!}
