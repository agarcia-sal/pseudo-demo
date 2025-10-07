import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    current_divisor: int = 2
    limit: int = math.isqrt(integer_n) + 1  # Use isqrt for integer sqrt

    while current_divisor <= limit:
        if integer_n % current_divisor == 0:
            factors.append(current_divisor)
            integer_n //= current_divisor
            limit = math.isqrt(integer_n) + 1
        else:
            current_divisor += 1
    if integer_n > 1:
        factors.append(integer_n)
    return factors