from typing import Union

def iscube(integer_a: int) -> bool:
    absolute_a = abs(integer_a)
    cube_root = round(absolute_a ** (1/3))
    cube = cube_root ** 3
    return cube == absolute_a