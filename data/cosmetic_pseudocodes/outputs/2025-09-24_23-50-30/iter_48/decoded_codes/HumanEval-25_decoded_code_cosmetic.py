import math
from typing import List


def factorize(arg_p: int) -> List[int]:
    results_q: List[int] = []
    index_r: int = 2
    while True:
        if index_r > math.isqrt(arg_p) + 1:
            break
        if arg_p % index_r == 0:
            results_q.append(index_r)
            arg_p //= index_r
        else:
            index_r += 1
    if arg_p > 1:
        results_q.append(arg_p)
    return results_q