def digits(a: int) -> int:
    b: int = 1
    c: int = 0
    d: int = 0
    s: str = str(a)
    while d < len(s):
        e: int = int(s[d])
        if e % 2 != 0:
            b *= e
            c += 1
        d += 1
    if c == 0:
        return 0
    return b