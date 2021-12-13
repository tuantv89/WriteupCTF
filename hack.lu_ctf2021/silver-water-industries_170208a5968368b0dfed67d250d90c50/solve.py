from pwn import remote
import gmpy2

address = ("flu.xxx", 20060)

conn = remote(address[0], address[1])

rcv = conn.recvline().strip()
n = int(rcv)

# Receive all bytes of the ciphertext
byteArr = []
for _ in range(20):
    byte = list(map(int, conn.recvline().decode().strip().strip("[").strip("]").split()))
    byteArr.append(byte)

token = b""
for byte in byteArr:
    bits = ""
    for bit in byte:
        # Jacobi symbol
        if gmpy2.jacobi(bit, n) == -1:
            bits += "1"
        else:
            bits += "0"
    token += bytes.fromhex(hex(int(bits, 2))[2:])

conn.sendline(token)
conn.interactive()
#flag{Oh_NO_aT_LEast_mY_AlGORithM_is_ExpanDiNg}
