

# This file was *autogenerated* from the file CSAW2021/quiz4PartialKeyExposure.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0p3 = RealNumber('0.3'); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_61354328725009110904662716659275242271539889771836075265120152113937032313555999117290122334833702089021667071225349870242496497666062752197929262832754362704460251233727815272161214664274657287725743695980286290326940956179914439969975329836770894979963849511231067481448088547959309648091922398434312801709 = Integer(61354328725009110904662716659275242271539889771836075265120152113937032313555999117290122334833702089021667071225349870242496497666062752197929262832754362704460251233727815272161214664274657287725743695980286290326940956179914439969975329836770894979963849511231067481448088547959309648091922398434312801709); _sage_const_17 = Integer(17); _sage_const_6393405926571965174437427296225243708127507777129441993689620203971856563385166021940469533780346193122725442072543477661100605090969221838194389428902929 = Integer(6393405926571965174437427296225243708127507777129441993689620203971856563385166021940469533780346193122725442072543477661100605090969221838194389428902929); _sage_const_0p5 = RealNumber('0.5'); _sage_const_7 = Integer(7)#user/bin/sage

def partial_p(p0, kbits, n):
    PR = PolynomialRing(Zmod(n), names=('x',)); (x,) = PR._first_ngens(1)
    nbits = n.nbits()
    f = _sage_const_2 **kbits*x + p0
    f = f.monic()
    roots = f.small_roots(X=_sage_const_2 **(nbits//_sage_const_2 -kbits), beta=_sage_const_0p3 )  # find root < 2^(nbits//2-kbits) with factor >= n^0.3
    if roots:
        x0 = roots[_sage_const_0 ]
        p = gcd(_sage_const_2 **kbits*x0 + p0, n)
        return ZZ(p)
def find_p(d0, kbits, e, n):
    X = var('X')
    for k in range(_sage_const_1 , e+_sage_const_1 ):
        results = solve_mod([e*d0*X - k*X*(n-X+_sage_const_1 ) + k*n == X], _sage_const_2 **kbits)
        for x in results:
            p0 = ZZ(x[_sage_const_0 ])
            p = partial_p(p0, kbits, n)
            if p:
                return p
if __name__ == '__main__':
    n = _sage_const_61354328725009110904662716659275242271539889771836075265120152113937032313555999117290122334833702089021667071225349870242496497666062752197929262832754362704460251233727815272161214664274657287725743695980286290326940956179914439969975329836770894979963849511231067481448088547959309648091922398434312801709 
    e = _sage_const_17 
    d = _sage_const_6393405926571965174437427296225243708127507777129441993689620203971856563385166021940469533780346193122725442072543477661100605090969221838194389428902929 
    beta = _sage_const_0p5 
    epsilon = beta**_sage_const_2 /_sage_const_7 
    nbits = n.nbits()
    # print ("nbits:%d:"%(nbits))
    # kbits = floor(nbits*(beta^2+epsilon))
    kbits = nbits - d.nbits()-_sage_const_1 
    # print ("kbits:%d"%(kbits))
    d0 = d & (_sage_const_2 **kbits-_sage_const_1 )
    # print ("lower %d bits (of %d bits) is given" % (kbits, nbits))
    p = find_p(d0, kbits, e, n)
    # print ("found p: %d" % p)
    q = n//p
    # print (d)
print(inverse_mod(e, (p-_sage_const_1 )*(q-_sage_const_1 )))

