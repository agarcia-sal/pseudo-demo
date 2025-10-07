from typing import Union

def iscube(a: Union[int, float]) -> bool:
    a_abs: float = abs(a)
    cube_root: int = round(a_abs ** (1/3))
    return cube_root ** 3 == a_abs