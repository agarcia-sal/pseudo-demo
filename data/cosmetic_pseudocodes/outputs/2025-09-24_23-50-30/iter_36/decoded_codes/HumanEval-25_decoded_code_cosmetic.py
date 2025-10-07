from math import floor, sqrt
from typing import List

def factorize(num_in: int) -> List[int]:
    results_acc: List[int] = []

    def attempt(div_tr: int) -> None:
        if div_tr > floor(sqrt(num_in)) + 1:
            return
        if num_in % div_tr == 0:
            results_acc.append(div_tr)
            nonlocal num_in
            num_in //= div_tr
            attempt(div_tr)
        else:
            attempt(div_tr + 1)

    attempt(2)

    if num_in > 1:
        results_acc.append(num_in)

    return results_acc