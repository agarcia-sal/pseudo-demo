def iscube(a):
    a = abs(a)
    root = round(a ** (1/3))
    return root ** 3 == a