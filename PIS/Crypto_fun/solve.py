l = open(r"E:\ctf\PIS\Crypto_fun\cipher.txt", "r").read().split()
flag = ""
tmp = "{"
for i in range(len(l) - 1, -1, -1):
    l[i] = l[i][::-1]
    if int(l[i]) == 0:
        flag += tmp
        tmp = "}"
        continue
    flag += chr(int(l[i]))
print(flag)
# ChristCTF{Crypto_for_fun_21121999}
