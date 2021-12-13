from Crypto.Cipher import DES3
key = "6b696d696461796f6f6b696d697761616e616e6461796f6f"
iv = "a070ae09a4b7627c"
ct = "59878c3b0190e5161228edb871d44514e761971ab39cd5bfc675050862ea2a0611751867e99ab2d5643b5689e893bf7ca76bc10777030a6a"
iv = bytes.fromhex(iv)
ct = bytes.fromhex(ct)
key = bytes.fromhex(key)
# print(key)
# print(iv)
# print(ct)
de = DES3.new(key, DES3.MODE_OFB, iv)
count = 0
pt = de.decrypt(ct)
print(pt)
