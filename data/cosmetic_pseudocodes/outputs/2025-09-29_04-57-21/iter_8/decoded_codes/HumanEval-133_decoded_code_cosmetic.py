import math
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    total_value: int = 0
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current: float = list_of_numbers[iterator]
        raised: int = math.ceil(current)
        squared_val: int = raised * raised
        total_value += squared_val
        iterator += 1
    return total_value