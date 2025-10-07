from math import isqrt
from typing import List

def factorize(input_value: int) -> List[int]:
    prime_components: List[int] = []
    candidate: int = 2
    limit: int = isqrt(input_value) + 1
    while candidate <= limit:
        if input_value % candidate == 0:
            prime_components.append(candidate)
            input_value //= candidate
            limit = isqrt(input_value) + 1  # update limit as input_value changes
        else:
            candidate += 1
    if input_value > 1:
        prime_components.append(input_value)
    return prime_components