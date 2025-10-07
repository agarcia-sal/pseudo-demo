from math import ceil
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared: int = 0
    for i in lst:
        squared += ceil(i) ** 2
    return squared