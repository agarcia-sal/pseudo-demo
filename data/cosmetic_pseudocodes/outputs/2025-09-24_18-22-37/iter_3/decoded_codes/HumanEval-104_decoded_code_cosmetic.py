from math import log10, floor
from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def helper_all_odd_digits(number: int, index: int) -> bool:
        if index < 0:
            return True
        digit = (number // (10**index)) % 10
        if digit % 2 == 0:
            return False
        return helper_all_odd_digits(number, index - 1)

    if not list_of_positive_integers:
        return []
    length = floor(log10(max(list_of_positive_integers))) + 1
    result_list = [
        num for num in list_of_positive_integers
        if helper_all_odd_digits(num, length - 1)
    ]
    return sorted(result_list)