def iscube(a) -> bool:
    a = abs(a)
    cube_root = round(a ** (1/3))
    cube_root_integer = int(cube_root)
    cube_of_root = cube_root_integer ** 3
    return cube_of_root == a