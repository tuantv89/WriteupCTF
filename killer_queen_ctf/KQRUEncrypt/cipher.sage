import random

Zx.<x> = ZZ[]
d = 7

def cyclicconvolution(f,g):
    return (f * g) % (x^n-1)

def balancedmod(f,q):
    g = list( ((f[i] + q//2) % q) - q//2 for i in range(n) )
    return Zx(g)

def rpoly():
    assert d <= n
    result = n*[0]
    for j in range(d):
        while True:
                r = randrange(n)
                if not result[r]: break
        result[r] = 1-2*randrange(2)
    return Zx(result)

def invertmodprime(f,p):
    T = Zx.change_ring(Integers(p)).quotient(x^n-1)
    return Zx(lift(1 / T(f)))


def invertmodpowerof2(f,q):
    assert q.is_power_of(2)
    g = invertmodprime(f,2)
    while True:
        r = balancedmod(cyclicconvolution(g,f),q)
        if r == 1: return g
        g = balancedmod(cyclicconvolution(g,2 - r),q)

def keypair():
    while True:
        try:
            f = rpoly()
            fp = invertmodprime(f, p)
            fq = invertmodpowerof2(f, q)
            break
        except:
            pass
    g = rpoly()
    publickey = balancedmod(p * cyclicconvolution(fq, g), q)
    secretkey = (f, fp)
    return (publickey, secretkey)

def encrypt(message, publickey):
    r = rpoly()
    return balancedmod(cyclicconvolution(publickey, r) + message, q)

def genMessage(message):
    m = Zx([
        (1 if random.random() <= 0.5 else -1)*int(c) for c in ''.join(format(ord(x), 'b').zfill(8) for x in message)
    ])
    return m

n = 161
p = 3
q = 128

with open("flag.txt","r") as f:
    m = genMessage(f.readline())

(publickey, secretkey) = keypair()
c = encrypt(m, publickey)

print("n =",n)
print()
print("p =",p)
print()
print("q =",q)
print()
print("Ciphertext =",c)
print()
print("Publickey =",publickey)