from typing import Union

def iscube(a: int) -> bool:
    a = abs(a)
    cubic_root = int(round(a ** (1 / 3)))
    cube_of_cubic_root = cubic_root * cubic_root * cubic_root
    return cube_of_cubic_root == a