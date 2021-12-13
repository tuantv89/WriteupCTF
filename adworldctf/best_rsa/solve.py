from Crypto.Util.number import GCD, isPrime, long_to_bytes,bytes_to_long
from Crypto.PublicKey import RSA
import gmpy2
k1 = open(r"E:\ctf\adworldctf\best_rsa\publickey1.pem","r").read().strip()
k2 = open(r"E:\ctf\adworldctf\best_rsa\publickey2.pem", "r").read().strip()
k1=RSA.import_key(k1)
k2=RSA.import_key(k2)
n1=k1.n
e1=k1.e
n2=k2.n
e2=k2.e
c1 = open(r"E:\ctf\adworldctf\best_rsa\cipher1.txt","rb").read().strip()
c2 = open(r"E:\ctf\adworldctf\best_rsa\cipher2.txt", "rb").read().strip()
c1=bytes_to_long(c1)
c2=bytes_to_long(c2)
g,x,y=gmpy2.gcdext(e1,e2)
ans=pow(c1,x,n1)*pow(c2,y,n2)
ans=ans%n1
print(long_to_bytes(ans))