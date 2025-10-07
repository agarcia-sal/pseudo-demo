from math import fabs

def iscube(a: int) -> bool:
    a = abs(a)
    cube_root = round(a ** (1 / 3))
    return cube_root ** 3 == a