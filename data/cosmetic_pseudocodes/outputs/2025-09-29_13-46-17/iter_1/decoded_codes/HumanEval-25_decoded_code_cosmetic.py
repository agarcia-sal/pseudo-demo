from math import sqrt, floor
from typing import List

def factorize(integer_n: int) -> List[int]:
    list_of_factors: List[int] = []
    divisor_i: int = 2
    while divisor_i <= floor(sqrt(integer_n)) + 1:
        if integer_n % divisor_i == 0:
            list_of_factors.append(divisor_i)
            integer_n //= divisor_i
        else:
            divisor_i += 1
    if integer_n > 1:
        list_of_factors.append(integer_n)
    return list_of_factors