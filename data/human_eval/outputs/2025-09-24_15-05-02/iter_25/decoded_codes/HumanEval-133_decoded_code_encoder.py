import math
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    squared: int = 0
    for element in list_of_numbers:
        ceiling_value: int = math.ceil(element)
        squared += ceiling_value ** 2
    return squared