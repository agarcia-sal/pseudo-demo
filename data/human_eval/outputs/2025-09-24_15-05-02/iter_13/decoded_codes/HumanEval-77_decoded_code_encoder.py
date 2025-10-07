def iscube(a):
    a = abs(a)
    return round(a ** (1 / 3)) ** 3 == a