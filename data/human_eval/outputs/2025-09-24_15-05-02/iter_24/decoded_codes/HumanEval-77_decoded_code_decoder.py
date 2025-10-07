from typing import Union

def iscube(a: Union[int, float]) -> bool:
    a = abs(a)
    if a == 0:
        return True  # 0 is a perfect cube (0^3)
    cube_root_approximation = round(a ** (1 / 3))
    return cube_root_approximation ** 3 == a