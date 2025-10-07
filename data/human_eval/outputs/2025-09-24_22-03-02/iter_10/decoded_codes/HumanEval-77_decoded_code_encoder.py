def iscube(a) -> bool:
    a = abs(a)
    return round(a ** (1 / 3)) ** 3 == a