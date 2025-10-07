from typing import Union


def iscube(a: Union[int, float]) -> bool:
    a_abs = abs(a)
    cube_root_approx = round(a_abs ** (1 / 3))
    return cube_root_approx ** 3 == a_abs