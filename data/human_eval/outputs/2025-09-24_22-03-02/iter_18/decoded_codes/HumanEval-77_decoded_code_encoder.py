def iscube(a: int) -> bool:
    a = abs(a)
    cube_root = round(a ** (1/3))
    cube_root_int = int(cube_root)
    cube_value = cube_root_int ** 3
    return cube_value == a