def iscube(a: int) -> bool:
    a = abs(a)
    cube_root = round(a ** (1/3))
    cube_root_int = int(cube_root)
    cube = cube_root_int ** 3
    return cube == a