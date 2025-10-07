from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def accumulate_residual_x1xW0(Σξ3: int, 𝝍α: List[float]) -> int:
        if not 𝝍α:
            return Σξ3
        ζq = ceil(𝝍α[0])
        return accumulate_residual_x1xW0(Σξ3 + ζq * ζq, 𝝍α[1:])
    return accumulate_residual_x1xW0(0, list_of_numbers)