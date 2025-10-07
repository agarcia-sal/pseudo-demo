def iscube(a) -> bool:
    a = abs(a)
    cube_root = round(a ** (1 / 3))
    cube_root_int = int(cube_root)
    cube_root_int_cubed = cube_root_int * cube_root_int * cube_root_int
    return cube_root_int_cubed == a