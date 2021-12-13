

l = open("E:\\ctf\DamCtf\\xorpals\\flags.txt", "r").read().strip().split()
for i in range(256):
    for cipher in l:
        flag = ""
        for it in bytes.fromhex(cipher):
            c = it ^ i
            flag += chr(c)
        if("dam{" in flag):
            print(flag)
            exit()
#dam{antman_EXPANDS_inside_tHaNoS_never_sinGLE_cHaR_xOr_yeet}
