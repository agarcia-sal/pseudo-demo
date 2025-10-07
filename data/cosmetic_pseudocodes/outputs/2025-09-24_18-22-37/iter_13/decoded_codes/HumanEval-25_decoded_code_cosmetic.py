from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_collection: List[int] = []
    current_divisor: int = 2
    threshold: int = int(sqrt(integer_n) + 1)
    while True:
        if current_divisor > threshold:
            break
        remainder_check: int = integer_n % current_divisor
        if remainder_check == 0:
            factors_collection.append(current_divisor)
            integer_n //= current_divisor
            threshold = int(sqrt(integer_n) + 1)
        else:
            current_divisor += 1
    if integer_n > 1:
        factors_collection.append(integer_n)
    return factors_collection