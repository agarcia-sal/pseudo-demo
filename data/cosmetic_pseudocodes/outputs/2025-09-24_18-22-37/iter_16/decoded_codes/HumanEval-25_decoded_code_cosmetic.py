import math
from typing import List

def factorize(kappa: int) -> List[int]:
    factors_collection: List[int] = []
    candidate_divisor: int = 2
    limit_value: int = int(math.isqrt(kappa)) + 1  # math.isqrt gives floor(sqrt(kappa))

    while candidate_divisor <= limit_value:
        modulus_remainder = kappa % candidate_divisor
        if modulus_remainder == 0:
            factors_collection.append(candidate_divisor)
            kappa //= candidate_divisor
            limit_value = int(math.isqrt(kappa)) + 1
        else:
            candidate_divisor += 1

    if kappa > 1:
        factors_collection.append(kappa)

    return factors_collection