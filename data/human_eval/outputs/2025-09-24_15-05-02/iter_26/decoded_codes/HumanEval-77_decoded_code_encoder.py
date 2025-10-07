from typing import Union

def iscube(integer_a: int) -> bool:
    absolute_a: int = abs(integer_a)
    if absolute_a == 0:
        return True  # 0 is a perfect cube (0^3)
    cube_root: int = round(absolute_a ** (1/3))
    return cube_root ** 3 == absolute_a