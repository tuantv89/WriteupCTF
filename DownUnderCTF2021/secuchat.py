
# import sqlite3

# from Crypto.Cipher import AES, PKCS1_OAEP
# from Crypto.PublicKey import RSA
# from Crypto.Util.number import bytes_to_long, long_to_bytes
# import gmpy2
# con = sqlite3.connect("./secuchat.db")
# cur = con.cursor()

# cur.execute("select username, rsa_key from user")
# tmp = cur.fetchall()

# ns = []
# es = []
# for t in tmp:
#     rsa = RSA.import_key(t[1])
#     ns.append(rsa.n)
#     es.append(rsa.e)

# for i in range(len(tmp)):
#     for j in range(i+1, len(tmp)):
#         g = gmpy2.gcd(ns[i], ns[j])
#         if g > 1:
#             print(i, j, g)
# # ns[1], ns[23] の gcd が 1 こえ
# # 1: hortonashley, 23: eriksaunders
# p1 = int(gmpy2.gcd(ns[1], ns[23]))
# p23 = p1
# q1 = ns[1] // p1
# q23 = ns[23] // p23
# phi1 = (p1 - 1) * (q1 - 1)
# e = 65537
# d1 = int(gmpy2.invert(e, phi1))

# rsa1 = RSA.construct((ns[1], e, d1, p1, q1))

# cipher = PKCS1_OAEP.new(rsa1)

# # conversation=46 で initiator=hortonashley, initial_parameters=328
# cur.execute("SELECT * FROM Message WHERE conversation=46")
# conv_init_1 = cur.fetchall()
# # print(len(conv_init_1))
# parameters = list(range(328, 328+len(conv_init_1)))
# aes_keys = []
# ivs = []
# for parameter in parameters:
#     cur.execute("SELECT * FROM Parameters WHERE id=?", (parameter,))
#     tmp = cur.fetchall()
#     init_enc_key = tmp[0][1]
#     iv = tmp[0][-1]
#     init_key = cipher.decrypt(init_enc_key)
#     aes_keys.append(init_key)
#     ivs.append(iv)

# for i in range(len(conv_init_1)):
#     aes = AES.new(aes_keys[i], AES.MODE_CBC, ivs[i])
#     print(aes.decrypt(conv_init_1[i][-1]))
# con.close()

import sqlite3
import itertools
from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

con = sqlite3.connect("./secuchat.db")
cur = con.cursor()

cur.execute("SELECT * FROM User;")
users = [(name, RSA.importKey(k)) for name, k in cur]
for (an, ak), (bn, bk) in itertools.combinations(users, 2):
    if (p := gcd(ak.n, bk.n)) > 1:
        break

print(an, bn)
ak = RSA.construct(
    (ak.n, 65537, pow(65537, -1, (p - 1) * ((q := (ak.n // p)) - 1)), p, q))
bk = RSA.construct(
    (bk.n, 65537, pow(65537, -1, (p - 1) * ((q := (bk.n // p)) - 1)), p, q))


for user, rsa_key in [(an, ak), (bn, bk)]:
    oaep = PKCS1_OAEP.new(rsa_key)
    cur.execute('''
        SELECT
            Conversation.id,
            initiator,
            peer,
            encrypted_aes_key_for_initiator,
            encrypted_aes_key_for_peer,
            iv
        FROM Conversation
        INNER JOIN Parameters
            ON Parameters.id = Conversation.initial_parameters
        WHERE initiator = ? OR peer = ?;
    ''', (user, user))

    for cid, initiator, peer, initiator_key, peer_key, iv in cur.fetchall():
        print(f"{cid}: {initiator} & {peer}")
        attribute = ""
        aes = None
        if initiator == user:
            attribute = "encrypted_aes_key_for_initiator"
            aes = AES.new(oaep.decrypt(initiator_key), AES.MODE_CBC, iv=iv)
        else:
            attribute = "encrypted_aes_key_for_peer"
            aes = AES.new(oaep.decrypt(peer_key), AES.MODE_CBC, iv=iv)

        cur.execute('''
        SELECT
            encrypted_message,
            from_initiator,
        ''' + f"{attribute}, " + '''
            iv
        FROM Message
        INNER JOIN Parameters
            ON Parameters.id = next_parameters
        WHERE conversation = ?
        ORDER BY
            timestamp ASC;
        ''', (cid,))
        for message, from_initiator, key, iv in cur.fetchall():
            print(f"{[peer, initiator][from_initiator]}:", message :=
                  unpad(aes.decrypt(message), AES.block_size).decode())
            if "DUCTF" in message:
                break

            aes = AES.new(oaep.decrypt(key), AES.MODE_CBC, iv=iv)
        if "DUCTF" in message:
            break

    if "DUCTF" in message:
        break

con.close()
