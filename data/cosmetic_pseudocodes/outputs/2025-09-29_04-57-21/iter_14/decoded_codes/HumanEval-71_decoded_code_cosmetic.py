from math import sqrt
from typing import Union


def triangle_area(side_a: float, side_b: float, side_c: float) -> Union[float, int]:
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return -1

    p_half: float = (side_c + side_b + side_a) / 2

    first_term: float = p_half
    second_term: float = p_half - side_a
    third_term: float = p_half - side_b
    fourth_term: float = p_half - side_c

    raw_area: float = sqrt(first_term * second_term * third_term * fourth_term)

    final_output: float = round(raw_area, 2)
    return final_output