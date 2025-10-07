def modp(a: int, b: int) -> int:
    c: int = 1
    d: int = 0
    while d < a:
        c = (c * 2) % b
        d += 1
    return c