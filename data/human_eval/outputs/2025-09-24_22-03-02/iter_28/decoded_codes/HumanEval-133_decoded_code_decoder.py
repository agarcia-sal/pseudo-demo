import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        ceiled_element = math.ceil(element)
        squared += ceiled_element * ceiled_element
    return squared