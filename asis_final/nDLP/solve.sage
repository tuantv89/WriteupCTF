from factordb import factordb
g = 685780528648223163108441
n = 12588567055208488159342105634949357220607702491616160304212767442540158416811459761519218454720193189
y = 9136134187598897896238293762558529068838567704462064643828064439262538588237880419716728404254970025
conn = factordb.FactorDB(n)
conn.connect()
ps = conn.get_factor_list()

# i fell into a tiny trap here. say we have
# g^a == c mod p1
# g^b == c mod p2
# then do we have g^crt([a, b], [p1, p2]) == c mod p1p2?
# no!
# instead, we should solve x == a mod (p1 - 1) and x == b mod (p2 - 1) by FlT
rs = [discrete_log(Mod(y, p), Mod(g, p)) for p in ps] # remainders
x = crt(rs, [p - 1 for p in ps])
assert pow(g, x, n) == y
print(bytes.fromhex(hex(x)[2:]).decode())