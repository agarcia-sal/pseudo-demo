import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    prime_factors: List[int] = []
    candidate = 2
    while candidate <= math.isqrt(integer_n) + 1:
        if integer_n % candidate == 0:
            prime_factors.append(candidate)
            integer_n //= candidate
        else:
            candidate += 1
    if integer_n > 1:
        prime_factors.append(integer_n)
    return prime_factors