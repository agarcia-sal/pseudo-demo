def iscube(a: int) -> bool:
    a = abs(a)
    cube_root = round(a ** (1 / 3))
    cube_of_root = cube_root ** 3
    if cube_of_root == a:
        return True
    else:
        return False