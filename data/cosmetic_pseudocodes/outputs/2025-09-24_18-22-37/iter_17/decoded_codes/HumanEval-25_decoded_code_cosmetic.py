from math import isqrt
from typing import List

def factorize(pseudonym_x: int) -> List[int]:
    aggregate_units: List[int] = []
    probe_var: int = 2
    boundary_limit: int = isqrt(pseudonym_x) + 1
    while probe_var <= boundary_limit:
        remainder_check = pseudonym_x % probe_var
        if remainder_check != 0:
            probe_var += 1
        else:
            aggregate_units.append(probe_var)
            pseudonym_x //= probe_var
            boundary_limit = isqrt(pseudonym_x) + 1
    if pseudonym_x > 1:
        aggregate_units.append(pseudonym_x)
    return aggregate_units