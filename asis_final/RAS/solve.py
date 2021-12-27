from Crypto.Util.number import *
l=[]
for a in range(2,512):
	for b in range(32,512):
		if(len(bin(a**b)[2:])==512):
			l.append(a**b)
			# print("a =",a)
			# print("b =",b)
			# print()

def partial_p(p0, n):  
    PR.<x> = PolynomialRing(Zmod(n))  
    nbits = n.nbits()  
    f = x + p0  
    f = f.monic()  
    roots = f.small_roots(X=2^(32), beta=0.3)  
    if roots:  
        x0 = roots[0]  
        p = gcd(x0 + p0, n)  
        return ZZ(p) 
c=11104433528952071860984483920122173351342473018268740572598132083816861855404615534742178674185812745207876206939230069251889172817480784782618716608299615251541018034321389516732611030641383571306414414804563863131355221859432899624060128497648444189432635603082478662202695641001726208833663163000227827283
n=56469405750402193641449232753975279624388972985036568323092258873756801156079913882719631252209538683205353844069168609565141017503581101845476197667784484712057287713526027533597905495298848547839093455328128973319016710733533781180094847568951833393705432945294907000234880317134952746221201465210828955449
for i in l:
	p0=i
	try:
		p=partial_p(p0,n)
		q=n//p
		if(p*q==n and isPrime(q) and isPrime(p)):
			print("p =",p)
			print("q =",q)
	except:
		pass
	

# p=7503181809956767523746965523445045476257163607925774521504848419053281285592652527357937939189782711610752940844746826826913644756871296753402980129494103
# q=7526061233844414054658272333288124411685335071877284335907504995816228844305448573362353388854643200579154642450347983868657774168720289858354259165638383
# e=65537
# d=inverse(e,(p-1)*(q-1))
# print(long_to_bytes(pow(c,d,n)))