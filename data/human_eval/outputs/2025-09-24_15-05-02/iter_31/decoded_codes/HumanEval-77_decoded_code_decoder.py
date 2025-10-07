def iscube(integer_value: int) -> bool:
    absolute_value = abs(integer_value)
    cube_root_approximation = round(absolute_value ** (1 / 3))
    return cube_root_approximation ** 3 == absolute_value