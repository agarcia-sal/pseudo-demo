from math import floor, sqrt
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor = 2
    while True:
        if current_divisor <= floor(sqrt(integer_n)) + 1:
            if integer_n % current_divisor != 0:
                current_divisor += 1
            else:
                factors_collection.append(current_divisor)
                integer_n //= current_divisor
        else:
            break
    if integer_n > 1:
        factors_collection.append(integer_n)
    return factors_collection