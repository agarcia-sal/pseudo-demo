def iscube(a: float) -> bool:
    a = abs(a)
    c = round(a ** (1 / 3))
    return c ** 3 == a