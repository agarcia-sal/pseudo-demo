def iscube(integer_value: int) -> bool:
    absolute_value = abs(integer_value)
    cube_root_approximation = round(absolute_value ** (1 / 3))
    cube_of_approximation = cube_root_approximation ** 3
    return cube_of_approximation == absolute_value