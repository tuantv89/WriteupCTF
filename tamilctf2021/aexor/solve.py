import binascii
from Crypto.Cipher import AES
from binascii import *
import string
from pwn import xor
enc = "030e150a0b0415110618111c001b0d1c"
ct = "68e934aa25be2c5f1674e101b31c25672400d69f9cf910a9f64071cea79f2de01d01bcf140105e5f7a3db66fffe64694"
iv = "1cb7942bf4ae14947150f9f196f92b2c"
iv = bytes.fromhex(iv)
enc = bytes.fromhex(enc)
print(enc)
ct = bytes.fromhex(ct)
# print(len(enc))
# plain = string.ascii_letters+string.digits+'_'
# print(len(plain))
sub_key = "okay"  # lol, fucking challenge
key = ""
for i in range(len(enc)):
    key += chr(enc[i] ^ ord(sub_key[i % len(sub_key)]))
key = key.encode()
decode = AES.new(key, AES.MODE_CBC, iv)
print(decode.decrypt(ct))
# def guess_key(i, j):
#     list = []
#     for a in plain:
#         for b in plain:
#             if xor(ord(a), enc[i]) == xor(ord(b) ^ enc[j]):
#                 list.append(chr(ord(a) ^ enc[i]))
#     return set(list)


# for a in range(1, 5):
#     print("try: ", a)
#     key_len = a
#     guess = ""
#     for i in range(key_len):
#         pre = i
#         next = i+key_len
#         if(next >= len(enc)):
#             break
#         print("running ", pre, end=" ")
#         print(next)
#         k = guess_key(pre, next)
#         pre = next
#         next += key_len
#         while(next < len(enc)):
#             print("running ", pre, end=" ")
#             print(next)
#             k = k.intersection(guess_key(pre, next))
#             pre = next
#             next += key_len
#         guess += '['+''.join(list(k))+']'
#     print(key_len, ":"+guess)
