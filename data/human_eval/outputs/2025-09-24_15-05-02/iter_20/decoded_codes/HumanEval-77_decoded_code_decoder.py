from typing import Union


def iscube(a: Union[int, float]) -> bool:
    absolute_value: float = abs(a)
    cube_root: int = round(absolute_value ** (1 / 3))
    return cube_root ** 3 == absolute_value