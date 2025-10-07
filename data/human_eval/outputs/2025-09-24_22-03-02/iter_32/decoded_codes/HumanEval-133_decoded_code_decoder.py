import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    squared = 0
    index = 0
    while index < len(lst):
        element = lst[index]
        ceiled_element = math.ceil(element)
        squared += ceiled_element * ceiled_element
        index += 1
    return squared