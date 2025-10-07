from math import sqrt, floor
from typing import List

def factorize(integer_n: int) -> List[int]:
    queue_of_factors: List[int] = []
    candidate_divisor = 2
    limit_bound = floor(sqrt(integer_n)) + 1
    while candidate_divisor <= limit_bound:
        if integer_n % candidate_divisor == 0:
            queue_of_factors.append(candidate_divisor)
            integer_n //= candidate_divisor
            limit_bound = floor(sqrt(integer_n)) + 1
        else:
            candidate_divisor += 1
    if integer_n > 1:
        queue_of_factors.append(integer_n)
    return queue_of_factors