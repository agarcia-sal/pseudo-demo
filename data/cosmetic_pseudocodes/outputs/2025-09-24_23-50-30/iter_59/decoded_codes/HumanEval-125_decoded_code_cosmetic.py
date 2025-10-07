from typing import Union, List


def split_words(a: str) -> Union[List[str], int]:
    if ' ' not in a:
        if ',' in a:
            b: List[str] = []
            c = 0
            while c < len(a):
                if a[c] == ',':
                    b.append(' ')
                else:
                    b.append(a[c])
                c += 1
            d = ''.join(b)
            return d.split()
        else:
            e = 0
            f = 0
            while f < len(a):
                g = a[f]
                if 'a' <= g <= 'z' and not (ord(g) % 2 != 0):
                    e += 1
                f += 1
            return e
    else:
        return a.split()