def digits(q: int) -> int:
    k: int = 1
    r: int = 0
    s: str = str(q)
    u: int = 0
    while u < len(s):
        v: str = s[u]
        w: int = int(v)
        x: int = w % 2
        if x == 0:
            u += 1
            continue
        elif x == 1:
            k *= w
            r += 1
            u += 1
    if r != 0:
        return k
    return 0