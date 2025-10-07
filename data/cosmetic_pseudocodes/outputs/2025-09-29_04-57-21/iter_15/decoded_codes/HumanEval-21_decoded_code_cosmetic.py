from typing import List
import math

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lower_bound: float = math.inf
    upper_bound: float = -math.inf
    pointer: int = 0
    length: int = len(list_of_numbers)

    while pointer < length:
        value = list_of_numbers[pointer]
        if value < lower_bound:
            lower_bound = value
        if value > upper_bound:
            upper_bound = value
        pointer += 1

    range_span: float = upper_bound - lower_bound
    if range_span == 0:
        # All elements are equal; avoid division by zero by returning zeros
        return [0.0 for _ in list_of_numbers]

    return [(element - lower_bound) / range_span for element in list_of_numbers]