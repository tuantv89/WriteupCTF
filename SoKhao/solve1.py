import base64
from Crypto.Util.number import long_to_bytes, bytes_to_long

AESblocksize = 16
authtoken = 'rdOgaqsHFSB3ast8k5eFlYHDaKfNRzlEZB+ObceT1Gw='
username = '123456789tuan'
role = 1

usernamebytes = username.encode('utf-8')
plainbytes = len(usernamebytes).to_bytes(2, "little") + \
    usernamebytes + role.to_bytes(1, "little")

encrypted_iv = base64.b64decode(authtoken)[:16]
cipher = base64.b64decode(authtoken)[16:]

key_and_iv = long_to_bytes(bytes_to_long(cipher) ^ bytes_to_long(plainbytes))

new_role = 0
new_plainbytes = len(usernamebytes).to_bytes(2, "little") + \
    usernamebytes + new_role.to_bytes(1, "little")

new_cipher = long_to_bytes(bytes_to_long(
    key_and_iv) ^ bytes_to_long(new_plainbytes))
new_authtoken = base64.b64encode(encrypted_iv + new_cipher)

print(new_authtoken)
# ASCIS{z3r0_l0g0n_1s_H3re}
