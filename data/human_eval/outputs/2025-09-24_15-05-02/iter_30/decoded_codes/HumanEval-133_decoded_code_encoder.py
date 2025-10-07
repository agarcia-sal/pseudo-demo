from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    squared = 0
    for number in list_of_numbers:
        rounded_number = math.ceil(number)
        squared += rounded_number * rounded_number
    return squared