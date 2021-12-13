
from Crypto.Util.number import long_to_bytes
ct = " jp pj jp pj jp pj jp jp  jp pj pj jp jp jp jp pj  jp pj pj jp pj pj jp pj  jp pj pj jp pj jp jp pj  jp pj pj jp pj pj jp jp  jp pj jp jp jp jp pj pj  jp pj jp pj jp pj jp jp  jp pj jp jp jp pj pj jp  jp pj pj pj pj jp pj pj  jp pj pj pj jp pj pj pj  jp pj pj jp pj jp jp jp  jp jp pj pj jp pj jp jp  jp pj pj pj jp pj jp jp  jp pj jp pj pj pj pj pj  jp pj pj pj jp pj jp jp  jp pj pj jp pj jp jp jp  jp jp pj pj jp jp pj pj  jp pj jp pj pj pj pj pj  jp pj pj jp jp jp pj jp  jp jp pj jp jp jp jp pj  jp jp pj pj jp pj jp jp  jp pj pj pj jp jp pj jp  jp pj pj pj pj jp jp pj  jp pj pj pj pj pj jp pj"
ct = ct.strip().split()
bin_cipher = ""
for i in ct:
    if i == "jp":
        bin_cipher += '0'
    else:
        bin_cipher += '1'
print(long_to_bytes(int(bin_cipher, 2)).decode())
