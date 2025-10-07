from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    squared_sum: int = 0
    for number in list_of_numbers:
        ceiling_value: int = math.ceil(number)
        squared_sum += ceiling_value ** 2
    return squared_sum