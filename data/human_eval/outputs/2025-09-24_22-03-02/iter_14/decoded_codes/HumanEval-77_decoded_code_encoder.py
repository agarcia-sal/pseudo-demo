def iscube(a: int) -> bool:
    a = abs(a)
    cube_root = int(round(a ** (1/3)))
    cube_of_root = cube_root ** 3
    return cube_of_root == a