import base64
import string
from Crypto.Util.strxor import strxor

plain=string.ascii_letters+string.digits+".?!'\",;: ()-"+chr(10)
#print(plain)

with open('cipher.txt', 'r') as f:
    cipher=base64.b64decode(f.read()).decode()

def enc(data, key):
    key = (key * (len(data) / len(key) + 1))[:len(data)]
    return strxor(data, key)

def guess_key(i,j):
    list=[]
    for a in plain:
        for b in plain:
            if ord(a) ^ ord(cipher[i]) == ord(b) ^ ord(cipher[j]) :
                list.append(chr(ord(a) ^ ord(cipher[i])))
    return set(list)
for a in range(1,25):
    key_len = a
    group = len(cipher) // key_len   
    key = ""
    for i in range(key_len):
        k = guess_key(0 * key_len + i, 1 * key_len + i)   
        for j in range(1, group-1):
            k = k & (guess_key(j * key_len + i, j * key_len + key_len + i))     
        key += "["+''.join(list(k))+"]"
    print(key_len,":"+key)



