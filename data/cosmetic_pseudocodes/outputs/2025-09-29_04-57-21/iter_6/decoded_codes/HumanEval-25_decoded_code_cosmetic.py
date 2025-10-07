from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    current_candidate = 2
    limit = int(sqrt(integer_n)) + 1
    while current_candidate <= limit:
        if integer_n % current_candidate == 0:
            factors.append(current_candidate)
            integer_n //= current_candidate
            limit = int(sqrt(integer_n)) + 1
        else:
            current_candidate += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors