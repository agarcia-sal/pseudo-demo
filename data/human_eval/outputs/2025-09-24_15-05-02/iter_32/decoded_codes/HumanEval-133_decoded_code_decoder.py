from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    sum_of_squares = 0
    for element in list_of_numbers:
        sum_of_squares += math.ceil(element) ** 2
    return sum_of_squares