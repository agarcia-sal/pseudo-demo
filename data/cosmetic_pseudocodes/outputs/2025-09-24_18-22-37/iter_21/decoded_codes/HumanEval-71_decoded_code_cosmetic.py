from math import sqrt
from typing import Union

def triangle_area(x1: float, y2: float, z3: float) -> Union[float, int]:
    if (x1 + y2) <= z3:
        return -1
    if (x1 + z3) <= y2:
        return -1
    if (y2 + z3) <= x1:
        return -1

    p_half: float = (x1 + y2 + z3) / 2
    temp1: float = p_half * (p_half - x1)
    temp2: float = (p_half - y2) * (p_half - z3)
    raw_area: float = sqrt(temp1 * temp2)
    final_result: float = round(raw_area, 2)
    return final_result