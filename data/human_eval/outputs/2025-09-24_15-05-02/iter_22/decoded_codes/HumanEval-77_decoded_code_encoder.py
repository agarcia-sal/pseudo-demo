from typing import Union

def iscube(integer_value: int) -> bool:
    absolute_value: int = abs(integer_value)
    cube_root_approximation: int = round(absolute_value ** (1 / 3))
    cube_of_approximation: int = cube_root_approximation ** 3
    return cube_of_approximation == absolute_value