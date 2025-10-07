import math
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    sum_of_squares = 0
    for element in list_of_numbers:
        ceiling_value = math.ceil(element)
        sum_of_squares += ceiling_value * ceiling_value
    return sum_of_squares