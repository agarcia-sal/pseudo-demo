import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for i in lst:
        ceil_value = math.ceil(i)
        square_of_ceil_value = ceil_value * ceil_value
        squared += square_of_ceil_value
    return squared