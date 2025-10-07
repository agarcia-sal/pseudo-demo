from math import sqrt, floor
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    divisor: int = 2
    limit: int = floor(sqrt(integer_n)) + 1
    while divisor <= limit:
        if integer_n % divisor == 0:
            factors.append(divisor)
            integer_n //= divisor
            limit = floor(sqrt(integer_n)) + 1  # update limit since integer_n changes
        else:
            divisor += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors