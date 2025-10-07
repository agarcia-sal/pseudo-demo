def iscube(a):
    a = abs(a)
    root = int(round(a ** (1/3)))
    cube = root ** 3
    return cube == a