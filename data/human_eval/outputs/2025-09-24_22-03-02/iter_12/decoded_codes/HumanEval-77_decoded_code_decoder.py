def iscube(a: float) -> bool:
    a = abs(a)
    return round(a ** (1/3)) ** 3 == a