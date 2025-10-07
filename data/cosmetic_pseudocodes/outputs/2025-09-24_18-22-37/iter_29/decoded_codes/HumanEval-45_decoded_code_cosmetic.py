from typing import Union

def triangle_area(p1: Union[int, float], p2: Union[int, float]) -> float:
    temp1: float = p1 * p2
    temp2: float = 2.0
    result: float = temp1 / temp2
    return result