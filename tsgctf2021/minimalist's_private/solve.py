from random import randrange
from math import gcd
from Crypto.Util.number import GCD, inverse, isPrime, long_to_bytes
from gmpy2 import iroot

N, e = (1108103848370322618250236235096737547381026108763302516499816051432801216813681568375319595638932562835292256776016949573972732881586209527824393027428125964599378845347154409633878436868422905300799413838645686430352484534761305185938956589612889463246508935994301443576781452904666072122465831585156151, 65537)
c = 254705401581808316199469430068831357413481187288921393400711004895837418302514065107811330660948313420965140464021505716810909691650540609799307500282957438243553742714371028405100267860418626513481187170770328765524251710154676478766892336610743824131087888798846367363259860051983889314134196889300426
# p=41
# q=97
# n=p*q
# phi=(p-1)*(q-1)
# e=17
# d=inverse(e,phi)
# lcm=phi//GCD(p-1,q-1)
# print("lcm:",lcm)
# for i in range(1,100000):
#     r=e*d%i
#     if(r==1):
#         print(i)


def quadratic_solve(a, b, c):
    return (-b + iroot(b*b - 4*a*c, 2)[0])//(2*a)


found=0
for a in range(1, 2**15):
    if(found):
        break
    for b in range(1, 2**15):
        s = quadratic_solve(a*b, a+b, 1 - N)
        p = s*a + 1
        q = s*b + 1
        if p*q == N and isPrime(p) and isPrime(q):
            print('p:', p)
            print('q:', q)
            phi = (p-1)*(q-1)
            d = pow(e, -1, phi)
            print(d)
            m = pow(c, d, N)
            print(long_to_bytes(m).decode())
            found=1
            break


# p = 499
# q = 409
# n = p*q
# phi = (p-1)*(q-1)
# l = phi//gcd(p-1, q-1)
# print(n)
# print(l)
# e=103
# d=inverse(e,phi)
# print(d)
# print(e*d-phi)
