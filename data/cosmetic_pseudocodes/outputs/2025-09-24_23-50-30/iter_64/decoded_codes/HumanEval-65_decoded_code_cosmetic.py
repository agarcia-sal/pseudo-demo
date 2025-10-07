def circular_shift(a: object, b: int) -> str:
    c: str = str(a)
    d: int = len(c)
    if b > d:
        return c[::-1]
    else:
        e: int = d - b
        f: str = c[e:d]
        g: str = c[0:e]
        return f + g