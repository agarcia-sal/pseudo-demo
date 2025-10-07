from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    result: int = 0
    for num in list_of_numbers:
        rounded_num: int = ceil(num)
        squared_num: int = rounded_num * rounded_num
        result += squared_num
    return result