from typing import Union


def iscube(num: Union[int, float]) -> bool:
    val: float = -num if num < 0 else num
    root: int = round(val ** (1 / 3))
    temp: int = root * root * root
    return temp == val