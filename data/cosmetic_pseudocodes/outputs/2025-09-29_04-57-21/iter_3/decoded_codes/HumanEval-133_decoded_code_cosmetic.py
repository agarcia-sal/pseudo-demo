from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    total: int = 0
    for index in range(len(list_of_numbers)):
        current_number: float = list_of_numbers[index]
        rounded_up: int = math.ceil(current_number)
        square_val: int = rounded_up * rounded_up
        total += square_val
    return total