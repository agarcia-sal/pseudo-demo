def iscube(a: int) -> bool:
    absolute_a = abs(a)
    cube_root_approx = round(absolute_a ** (1 / 3))
    return cube_root_approx ** 3 == absolute_a