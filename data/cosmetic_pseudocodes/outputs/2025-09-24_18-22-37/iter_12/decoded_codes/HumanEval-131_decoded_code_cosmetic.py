def digits(m: int) -> int:
    y: int = 0
    z: int = 1
    s: str = str(m)
    i: int = 0
    while i < len(s):
        p: int = int(s[i])
        if p % 2 == 1:
            z *= p
            y += 1
        i += 1
    if y == 0:
        return 0
    return z