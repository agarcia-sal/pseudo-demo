from math import sqrt
from typing import List, Tuple

def factorize(param_a: int) -> List[int]:
    collection_b: List[int] = []
    counter_c: int = 2

    def helper_d(value_e: int, limit_f: int, accum_g: List[int], base_h: int) -> Tuple[int, List[int]]:
        if value_e % base_h == 0:
            value_e //= base_h
            accum_g.append(base_h)
            return helper_d(value_e, limit_f, accum_g, base_h)
        else:
            if base_h <= limit_f:
                return helper_d(value_e, limit_f, accum_g, base_h + 1)
            else:
                return value_e, accum_g

    limit_j: int = 1 + int(sqrt(param_a))
    rem_k, collection_b = helper_d(param_a, limit_j, collection_b, counter_c)

    if rem_k > 1:
        collection_b.append(rem_k)

    return collection_b