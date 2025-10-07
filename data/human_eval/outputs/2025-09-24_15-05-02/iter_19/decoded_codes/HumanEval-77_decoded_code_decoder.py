def iscube(integer_a: int) -> bool:
    absolute_value: int = abs(integer_a)
    cube_root_approx: int = round(absolute_value ** (1 / 3))
    cube_of_approx: int = cube_root_approx ** 3
    return cube_of_approx == absolute_value