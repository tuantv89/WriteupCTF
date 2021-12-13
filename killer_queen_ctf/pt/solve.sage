import random
from mt19937predictor import MT19937Predictor
predictor = MT19937Predictor()
f = open("E:\ctf\killer_queen_ctf\pt\outputpt.txt","r")
arr=[]
for i in range(624):
    arr.append(int(f.readline().strip()))
for _ in range(624):
    predictor.setrandbits(arr[_], 512)

size = 2**20  # 1048576
with open("E:\\ctf\\killer_queen_ctf\\pt\\mersenneoutputs.txt", "r") as f:

    arr = [int(x) for x in f.readlines()]
    size = 2 ^ 20
    mo = arr[0]

    FR.<x> = PolynomialRing(IntegerModRing(mo), implementation="NTL")
    print("Running...")
    f = prod([(arr[_]*x-1) for _ in range(1, size)])
    print("Done!")
    R = Integers(mo)
    points = [R(arr[size+_]) for _ in range(size)]
    tree = [0 for i in range(size*2)]
    ft = [0 for i in range(size*2)]
    
    for i in range(size):
        tree[i+size] = (x-points[i])
        
    for i in range(size-1,0,-1):
        tree[i] = tree[i*2]*tree[i*2+1]
    
    ft[1] = f
    for i in range(2,size*2):
        ft[i] = ft[i//2]%tree[i]
 
    ans = prod(ft[size:size*2])
    print(ans)

    ciphertext = b'/\xbe\x9f\x83\x8a\x9eY\xb43\x9f\xfa\xc2\x98\xe9@K\xd7r\xd7j\xde\xd5\xef,\xda\x11\x1as\x83k\x10\xb8\xaaP\x7f \xb6|\xe02\x0fr\x0b\xf8\x9c\xfep2' # last line of outputpt.txt
    otp = bytearray.fromhex(hex(int(ans))[2:-10])
    
    plaintext = bytearray(b"")
    for i, c in enumerate(ciphertext):
        plaintext.append(c^^otp[i])
    
    print(plaintext)
    
#kqctf{p0lyn0m14l5_c4n_b3_v3ry_f457_0r_v3ry_5l0w}
