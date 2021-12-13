from os import read
import random
import binascii


def keygen(ln):
    # Generate a linearly independent key
    arr = [1 << i for i in range(ln)]
    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[j] ^= arr[i]
    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[ln - 1 - j] ^= arr[ln - 1 - i]

    return arr


def gen_keystream(key):
    ln = len(key)

    # Generate some fake values based on the given key...
    fake = [0] * ln
    for i in range(ln):
        for j in range(ln // 3):
            if i + j + 1 >= ln:
                break
            fake[i] ^= key[i + j + 1]
    print(fake)
    print()
    print()
    # Generate the keystream
    res = []
    for i in range(ln):
        t = random.getrandbits(1)
        if t:
            res.append((t, [fake[i], key[i]]))
        else:
            res.append((t, [key[i], fake[i]]))

    # Shuffle!
    random.shuffle(res)

    keystream = [v[0] for v in res]
    public = [v[1] for v in res]
    return keystream, public


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def recover_keystream(key, public):
    st = set(key)
    keystream = []
    for v0, v1 in public:
        if v0 in st:
            keystream.append(0)
        elif v1 in st:
            keystream.append(1)
        else:
            assert False, "Failed to recover the keystream"
    return keystream


def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res


def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)


s = "cd4c1a7edd7a421dcea72ae8bf47946d74f6cdba763a6a052a3f2955333dc6fa267f5297c405bf807e922380ebf9628194bf319e8ae4074dc5476de1d81a52d72c29f0e8b590ac8f6a78bb"


def find(public, x):
    for i in range(len(public)):
        if(x == public[i][0]):
            return public[i][1]
        elif(x == public[i][1]):
            return public[i][0]


f = open("E:\ctf\pbctf\Alkaloid Stream\output.txt", "r").read().strip()
public1 = []
f = list(f.split("],"))
public = []
for i in range(len(f)):
    temp = f[i].strip()
    temp = list(temp.split(","))
    public.append([int(temp[0][1:]), int(temp[1].strip())])

key = []
key.append(find(public, 0))
k1 = 2757696071210081807360560576412795699230755024318763149013967339353762389921680057821717495151761096162627419558972312206286782426655299773478926876284074659695710535424355133843847
key.append(k1)
while(len(key) < 600):
    limit = min(len(key), 200)
    index = len(key)-1
    x = 0
    for i in range(limit):
        x ^= key[index]
        index -= 1
    key.append(find(public, x))

key.reverse()
keystream = recover_keystream(key, public)
cipher = binascii.unhexlify(s)
cipher = bytes_to_bits(cipher)
pt = bits_to_bytes(xor(cipher, keystream))
print(pt)
