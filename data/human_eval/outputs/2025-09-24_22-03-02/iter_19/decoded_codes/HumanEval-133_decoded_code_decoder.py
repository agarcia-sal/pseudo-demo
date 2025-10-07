from typing import List
import math

def sum_squares(lst: List[float]) -> int:
    squared = 0
    for i in range(len(lst)):
        element = lst[i]
        ceiled_element = math.ceil(element)
        squared_element = ceiled_element * ceiled_element
        squared += squared_element
    return squared