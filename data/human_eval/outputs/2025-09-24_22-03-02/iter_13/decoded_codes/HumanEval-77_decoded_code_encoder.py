def iscube(a) -> bool:
    a = abs(a)
    cube_root = int(round(a ** (1 / 3)))
    return cube_root ** 3 == a