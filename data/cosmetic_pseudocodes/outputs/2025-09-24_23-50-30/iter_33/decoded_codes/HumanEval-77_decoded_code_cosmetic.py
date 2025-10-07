def iscube(p: int) -> bool:
    a = abs(p)
    b = round(a ** (1 / 3))
    c = b * b * b
    return c == a