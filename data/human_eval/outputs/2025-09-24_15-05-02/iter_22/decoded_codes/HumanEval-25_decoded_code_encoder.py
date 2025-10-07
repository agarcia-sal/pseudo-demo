from math import floor, sqrt
from typing import List

def factorize(integer_number: int) -> List[int]:
    factors_list: List[int] = []
    divisor: int = 2
    while divisor <= floor(sqrt(integer_number)) + 1:
        if integer_number % divisor == 0:
            factors_list.append(divisor)
            integer_number //= divisor
        else:
            divisor += 1
    if integer_number > 1:
        factors_list.append(integer_number)
    return factors_list