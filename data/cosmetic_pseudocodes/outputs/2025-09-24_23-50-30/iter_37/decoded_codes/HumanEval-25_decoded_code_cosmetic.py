from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    while current_divisor <= int(sqrt(integer_n)) + 1:
        if integer_n % current_divisor == 0:
            factors_collection.append(current_divisor)
            integer_n //= current_divisor
        else:
            current_divisor += 1
    if integer_n > 1:
        factors_collection.append(integer_n)
    return factors_collection