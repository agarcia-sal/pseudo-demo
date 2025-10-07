from typing import Union


def triangle_area(length1: float, length2: float, length3: float) -> float:
    if not (length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1):
        return -1.0
    perimeter_half = (length1 + length2 + length3) * 0.5
    product = perimeter_half
    for current_length in (length1, length2, length3):
        product *= perimeter_half - current_length
    root_val = product ** 0.5
    final_result = round(root_val * 100) / 100
    return final_result