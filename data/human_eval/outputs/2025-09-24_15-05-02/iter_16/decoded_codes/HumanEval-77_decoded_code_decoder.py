from typing import Any

def iscube(integer_a: int) -> bool:
    absolute_a: int = abs(integer_a)
    cube_root_approx: int = round(absolute_a ** (1 / 3))
    return cube_root_approx ** 3 == absolute_a