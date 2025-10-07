def iscube(integer_value: int) -> bool:
    absolute_value = abs(integer_value)
    cube_root_estimate = round(absolute_value ** (1/3))
    cube_of_estimate = cube_root_estimate ** 3
    return cube_of_estimate == absolute_value