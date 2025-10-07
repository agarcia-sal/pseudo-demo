from math import sqrt
from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    # Check for the triangle inequality theorem
    if x1 + x2 <= x3 or x1 + x3 <= x2 or x2 + x3 <= x1:
        return -1  # Invalid triangle

    semip = (x1 + x2 + x3) / 2
    temp_area = semip * (semip - x1) * (semip - x2) * (semip - x3)
    area = sqrt(temp_area)
    outcome = round(area, 2)
    return outcome