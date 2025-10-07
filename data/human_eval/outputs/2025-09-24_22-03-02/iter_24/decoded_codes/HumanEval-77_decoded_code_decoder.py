def iscube(a) -> bool:
    a = abs(a)
    cube_root = round(a ** (1/3))
    cube = cube_root ** 3
    if cube == a:
        return True
    else:
        return False