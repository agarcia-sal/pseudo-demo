from typing import List, Union


def split_words(x: str) -> Union[List[str], int]:
    y: int = 0
    z: int = 0
    w: int = 0

    # Check if any of the first seven characters is a space (if x has fewer than 7 chars, check what is available)
    for idx in range(min(7, len(x))):
        if x[idx] == " ":
            z = 1
            break

    if z == 1:
        q: List[str] = []
        r: int = 0
        while r < len(x):
            if x[r] != " ":
                t: int = r
                while t < len(x) and x[t] != " ":
                    t += 1
                u: str = x[r:t]
                q.append(u)
                r = t
            else:
                r += 1
        return q
    else:
        o: int = 0
        while o < len(x):
            if x[o] == ",":
                w = 1
                break
            o += 1
        if w == 1:
            a: str = ""
            b: int = 0
            while b < len(x):
                if x[b] == ",":
                    a += " "
                else:
                    a += x[b]
                b += 1
            c: List[str] = []
            d: int = 0
            while d < len(a):
                if a[d] != " ":
                    e: int = d
                    while e < len(a) and a[e] != " ":
                        e += 1
                    f: str = a[d:e]
                    c.append(f)
                    d = e
                else:
                    d += 1
            return c

    h: int = 0
    i: int = 0
    while i < len(x):
        j: str = x[i]
        if "a" <= j <= "z":
            k: int = ord(j)
            l: int = k % 2
            if l == 0:
                h += 1
        i += 1
    return h