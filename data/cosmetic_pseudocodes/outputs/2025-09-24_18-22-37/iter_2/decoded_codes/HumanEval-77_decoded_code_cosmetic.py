from typing import Union


def iscube(num: int) -> bool:
    val: int = -num if num < 0 else num
    root: int = round(val ** (1 / 3))
    cube_check: int = root * root * root
    return cube_check == val