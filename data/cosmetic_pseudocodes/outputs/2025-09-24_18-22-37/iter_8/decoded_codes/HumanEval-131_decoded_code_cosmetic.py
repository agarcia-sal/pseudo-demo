def digits(q: int) -> int:
    y: str = str(q)
    s: int = 0
    w: int = 1

    p: int = 0
    while p < len(y):
        j: int = int(y[p])
        p += 1
        if j % 2 == 1:
            w *= j
            s += 1
    return w if s != 0 else 0