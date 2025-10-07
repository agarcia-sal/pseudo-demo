from math import sqrt
from typing import List

def factorize(number: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = int(sqrt(number)) + 1
    while candidate <= limit:
        if number % candidate == 0:
            factors.append(candidate)
            number //= candidate
            limit = int(sqrt(number)) + 1
        else:
            candidate += 1
    if number > 1:
        factors.append(number)
    return factors