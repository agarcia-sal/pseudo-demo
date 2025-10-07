from math import sqrt, floor
from typing import List

def factorize(param_a: int) -> List[int]:
    container_x: List[int] = []
    index_p: int = 2
    limit_q: int = floor(sqrt(param_a)) + 1

    while index_p <= limit_q:
        if param_a % index_p == 0:
            container_x.append(index_p)
            param_a //= index_p
            limit_q = floor(sqrt(param_a)) + 1  # Update limit since param_a changed
        else:
            index_p += 1

    if param_a > 1:
        container_x.append(param_a)

    return container_x