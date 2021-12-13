from Crypto.PublicKey import RSA
import gmpy2
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import *
f = """-----BEGIN PUBLIC KEY-----
MDgwDQYJKoZIhvcNAQEBBQADJwAwJAIdDVZLl4+dIzUElY7ti3RDcyge0UGLKfHs
+oCT2M8CAwEAAQ==
-----END PUBLIC KEY-----"""
public_key = RSA.importKey(f)
n = public_key.n
e = public_key.e
# print(n)
# print(e)
p = 17963604736595708916714953362445519
q = 20016431322579245244930631426505729
d = gmpy2.invert(e, (p-1)*(q-1))
# print(d)
ct = "C1qKLBtrUwLkebPf+JKX6ie1bKEdUGmzkYwBJWQ="
ct = b64decode(ct)
# print(ct)
c = bytes_to_long(ct)
part2 = long_to_bytes(pow(c, d, n))
n = 667
d = 1027
e = 3
part1 = (408, 217, 382, 380, 416, 613, 408, 162, 604, 9, 537, 146, 280)
flag = ""
for i in range(len(part1)):
    flag += long_to_bytes(pow(part1[i], d, n)).decode()
flag += part2[-9:].decode().strip()
print(flag)
