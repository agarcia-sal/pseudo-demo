def iscube(integer_a):
    integer_a = abs(integer_a)
    cube_root = round(integer_a ** (1 / 3))
    return cube_root ** 3 == integer_a