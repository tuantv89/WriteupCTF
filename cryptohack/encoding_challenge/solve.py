from pwn import * # pip install pwntools
import json
import codecs
from base64 import *
from binascii import unhexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes
r = remote('socket.cryptohack.org', 13377, level = 'debug')
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
for i in range(100):
    received = json_recv()

    print("Received type: ",end="")
    print(received["type"])
    print("Received encoded value: ",end="")
    print(received["encoded"])
    type=received["type"]
    enc=received["encoded"]
    decode=""
    if(type=="base64"):
        decode=b64decode(enc).decode()
    if(type=="hex"):
        decode=unhexlify(enc).decode()
    if(type=="rot13"):
        decode=codecs.decode(enc,'rot_13')
    if(type=="bigint"):
        decode=long_to_bytes(int(enc,16)).decode()
    if(type=="utf-8"):
        decode=[chr(b) for b in enc]
        decode="".join(decode)

    to_send = {
        "decoded": decode
    }
    json_send(to_send)
r.interactive()