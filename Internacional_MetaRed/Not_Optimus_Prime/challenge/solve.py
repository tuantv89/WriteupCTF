from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse, isPrime,GCD, long_to_bytes
key=[0]*50
e=65537
for i in range(50):
    path = "E:\\ctf\\Internacional_MetaRed\\Not_Optimus_Prime\\challenge\\public_key"+str(i)+".txt"
    key[i]=open(path,"r").read().strip()
    key[i]=RSA.import_key(key[i]).n
for i in range(50):
    for j in range(i+1,50):
        if(isPrime(GCD(key[i],key[j]))):
            print(i,end=" ")
            print("",j)
g=GCD(key[12],key[32])
cipher = open(r"E:\ctf\Internacional_MetaRed\Not_Optimus_Prime\challenge\cipher12.txt","rb").read().strip()
cipher=bytes_to_long(cipher)
p12=g
q12=key[12]//g
d12=inverse(e,(p12-1)*(q12-1))
print(long_to_bytes(pow(cipher,d12,key[12])))
#flag{C0mm0n_pr1m3s_gG!}
