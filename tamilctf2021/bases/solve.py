import base65536
from baseconv import base16, base56, base58, base64
from base64 import b32decode, a85decode
import base91
import base62
# import anybase32
# import base36
# from base64 import b85decode

# base65536 -> 91 -> 62 -> 32 ->85
# {16,32,56,62,64,a85,91,65536}
l = list(range(9))
found = 0
check = [1]*9


def Try(index, cipher):
    global found
    if found == 1:
        return
    if index == 0:
        try:
            ct = base16.decode(cipher)
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 1:
        try:
            ct = b32decode(cipher).decode()
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 2:
        try:
            ct = base56.decode(cipher)
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 3:
        try:
            ct = base58.decode(cipher)
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 4:
        try:
            ct = base62.decodebytes(cipher).decode()
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 5:
        try:
            ct = base64.decode(cipher)
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 6:
        try:
            ct = a85decode(cipher).decode()
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 7:
        try:
            ct = base91.decode(cipher).decode()
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass
    if index == 8:
        try:
            ct = base65536.decode(cipher).decode()
            if('TamilCTF{' in ct):
                found = 1
                print(ct)
                return
            for i in range(9):
                if(check[i] == 1):
                    check[i] = 0
                    Try(i, ct)
                    check[i] = 1
        except:
            pass


if __name__ == "__main__":
    cipher = open("./bases/cipher.txt", 'rb').read().strip().decode()
    # cipher = base65536.decode(cipher).decode()
    # print(cipher)
    # cipher = base91.decode(cipher).decode()
    # print(cipher)
    # cipher = base62.decodebytes(cipher).decode()
    # print(cipher)
    # cipher = b32decode(cipher).decode()
    # cipher = a85decode(cipher).decode()
    # print(cipher)

    for i in range(9):
        check[i] = 0
        Try(i, cipher)
        check[i] = 1
