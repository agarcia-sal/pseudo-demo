import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for index in range(len(lst)):
        value = lst[index]
        math_ceil_result = math.ceil(value)
        squared += math_ceil_result * math_ceil_result
    return squared