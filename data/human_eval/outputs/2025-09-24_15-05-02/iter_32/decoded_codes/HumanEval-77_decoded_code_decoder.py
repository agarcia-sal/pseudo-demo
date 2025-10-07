from typing import Union


def iscube(integer_value: int) -> bool:
    absolute_value = abs(integer_value)
    approximate_cube_root = round(absolute_value ** (1 / 3))
    cube_of_approximate_root = approximate_cube_root ** 3
    return cube_of_approximate_root == absolute_value