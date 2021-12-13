from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes,bytes_to_long
import gmpy2
c = 0x2085f3d3573cd709fad84bed9fe8dde419fb7c8e96aa95ec4651a3bc07b5552f321e03404943744d931a4a51a817cf190880a5efbf94aa828c45da5b31dcdefc

key = """-----BEGIN RSA PRIVATE KEY-----
MIIBOQIBAAJAf5g1ofh1ZBSB8XPZ6qTMdry5HIn6VSn4WrmBXwAaeOtzLzRaz+Tl
VR+0D0FkwiZ5K1cWs80nu31bqpAgQIGAUwIDAQABAkAXxZHodVPZq4ByLbVh5AY7
8PlD+ejryP/+VyVlP62u7VkNTowJOmzoAHxzbp1XW+S5RVfs0Dfpr161quGyc/jR
AiEA7ZZvfSVHFA59KP8jWsnbkle6zLhu3lYTBs5DqNInKv8CIQCJe5eXmfWfPbdK
XL+MTDdb9mnRluTq9yWjIJ2pbdCOrQIhANtMXCQbYHw203gf6DZI1A9EQvvr0QoQ
UQebJACT2etpAiAYH1pi3D2vmhmN76YgTMMt3JeGkc5Kt+CftbpUHxOH5QIgHJRH
dgDPAPcQmmwTgiMA4nseGVz011yFD2pojJmfF6g=
-----END RSA PRIVATE KEY-----"""
k=RSA.import_key(key)
n=k.n
# e=k.e
# print(n)
# print(e)
# print(c)
d=k.d
# p=k.p
# q=k.q
flag=long_to_bytes(pow(c,d,n)).decode()
flag=flag[::-1]
print(flag)