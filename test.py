import requests
e = 65537
from Crypto.Util.number import  inverse,long_to_bytes,bytes_to_long
# m = 14820437300756891031521271825877572034368691567980334773869022610196316836668210609918011764
# url = "https://rsabasics.board.kettlec.tf/encryption"
# s = requests.session()
# x = s.get(url)
# txt = x.text.strip().split(":")
# n = int(txt[-1][:-1])
# print(n)
# for i in range(10):
#     ans = str(pow(m, e, n))
#     data = {'answer': ans}
#     r = s.post(url, headers=x.headers, json=data)
#     out = r.text.strip()
#     print(out)
#     n = int(out.split(",")[-2][4:])
#     print(n)
#kettle_rsa_is_not_so_hard_if_you_read_wikipedia_lol
# n = 51002258323838958276412615209386964326812718164371563675339810664478007437693
# p = 320575045860732509666816440234340469001
# enc = 25774220127875571594806276092399411214246345637301172811503349103620755325636
# q=n//p
# phi=(p-1)*(q-1)
# d=inverse(e,phi)
# print(long_to_bytes(pow(enc,d,n)))
# mul = 17281371501504363994602849492681001619644901832582384813575
# m = 29862893681134883361798406196132397005733179295814546292287
# print(m*mul)
# x=308084236255353308374412848550510445576953304502978
# print(long_to_bytes(x//2))
n = 909636003379
enc = 633926349050
p = 871901
q = 1043279
phi=(p-1)*(q-1)
d=inverse(e,phi)
print(long_to_bytes(pow(enc,d,n)))
