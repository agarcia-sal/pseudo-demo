from typing import Union


def iscube(a: Union[int, float]) -> bool:
    a_abs: float = abs(a)
    if a_abs == 0:
        return True  # 0 is a perfect cube (0^3 = 0)
    cube_root: int = int(round(a_abs ** (1 / 3)))
    return cube_root ** 3 == a_abs