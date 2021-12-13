cipher = [
    8194393930139798,
    7130326565974613,
    9604891888210928,
    6348662706560873,
    11444688343062563,
    7335285885849258,
    3791814454530873,
    926264016764633,
    9604891888210928,
    5286663580435343,
    5801472714696338,
    875157765441840,
    926264016764633,
    2406927753242613,
    5980222734708251,
    5286663580435343,
    2822500611304865,
    5626320567751485,
    3660106045179536,
    2309834531980460,
    12010406743573553,
]
# solving using sagemath
x=ord('n')
y=ord('i')
z=ord('t')
t=ord('e')
# m = Matrix([[pow(x, 3), pow(x, 2), x, 1], [pow(y, 3),
#            pow(y, 2), y, 1], [pow(z, 3), pow(z, 2), z, 1], [pow(t, 3), pow(t, 2), t, 1]])
# v=vector([cipher[0],cipher[1],cipher[2],cipher[3]])
# print(m.solve_right(v))
a, b, c, d = 6096359484, 6606845234, 1736000027, 5669601428
flag = "nite"
import string

for j in range(4, len(cipher)):
    for i in string.printable:
        res = a * pow(ord(i), 3) + b * pow(ord(i), 2) + c * ord(i) + d
        if res == cipher[j]:
            flag += i
            break
print(flag)
# nite{jU5t_b45Ic_MaTH}
