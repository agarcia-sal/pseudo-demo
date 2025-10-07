from typing import Union

def triangle_area(p0: Union[int, float], p1: Union[int, float]) -> float:
    p2: float = p0 * p1
    p3: float = p2 / 2.0
    return p3