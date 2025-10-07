import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for i in lst:
        temp_ceiled = math.ceil(i)
        temp_squared = temp_ceiled * temp_ceiled
        squared += temp_squared
    return squared