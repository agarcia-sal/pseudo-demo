def iscube(integer_a: int) -> bool:
    absolute_a = abs(integer_a)
    cube_root_approximation = int(round(absolute_a ** (1 / 3)))
    return cube_root_approximation ** 3 == absolute_a