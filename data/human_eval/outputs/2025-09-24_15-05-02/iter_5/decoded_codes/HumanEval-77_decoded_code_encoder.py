def iscube(a):
    a = abs(a)
    cube_root_rounded = int(round(a ** (1 / 3)))
    return cube_root_rounded ** 3 == a