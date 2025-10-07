from math import ceil
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for i in lst:
        squared += ceil(i) * ceil(i)
    return squared