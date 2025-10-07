from typing import List
import math

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for i in lst:
        squared += math.ceil(i) * math.ceil(i)
    return squared