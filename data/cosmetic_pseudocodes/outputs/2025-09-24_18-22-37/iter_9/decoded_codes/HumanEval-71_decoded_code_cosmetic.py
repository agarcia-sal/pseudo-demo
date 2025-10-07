from math import sqrt
from typing import Union


def triangle_area(xp: float, yq: float, zk: float) -> Union[float, int]:
    valid_condition: bool = not ((xp + yq > zk) and (xp + zk > yq) and (yq + zk > xp))
    if valid_condition:
        return -1
    half_perimeter: float = (xp + yq + zk) / 2
    intermediate_expr: float = half_perimeter * (half_perimeter - xp) * (half_perimeter - yq) * (half_perimeter - zk)
    computed_area: float = sqrt(intermediate_expr)
    final_result: float = round(computed_area, 2)
    return final_result