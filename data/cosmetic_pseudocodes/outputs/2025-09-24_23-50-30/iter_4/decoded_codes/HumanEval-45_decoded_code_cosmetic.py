from typing import Union

def triangle_area(base: Union[int, float], altitude: Union[int, float]) -> float:
    if base != 0:
        area: float = (altitude * base) / 2.0
    else:
        area = 0.0
    return area