from typing import Union


def iscube(integer_a: int) -> bool:
    absolute_a: int = abs(integer_a)
    cube_root: int = round(absolute_a ** (1 / 3))
    return cube_root ** 3 == absolute_a