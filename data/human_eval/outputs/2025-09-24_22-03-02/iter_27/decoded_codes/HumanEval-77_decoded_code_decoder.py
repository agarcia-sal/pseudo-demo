def iscube(a):
    a = abs(a)
    cube_root = round(a ** (1 / 3))
    cube_root_cubed = cube_root ** 3
    if cube_root_cubed == a:
        return True
    else:
        return False