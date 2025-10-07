from math import sqrt
from typing import List


def factorize(input_number: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = int(sqrt(input_number) + 1)
    while candidate <= limit and input_number > 1:
        if input_number % candidate == 0:
            factors.append(candidate)
            input_number //= candidate
            limit = int(sqrt(input_number) + 1)
        else:
            candidate += 1
    if input_number > 1:
        factors.append(input_number)
    return factors