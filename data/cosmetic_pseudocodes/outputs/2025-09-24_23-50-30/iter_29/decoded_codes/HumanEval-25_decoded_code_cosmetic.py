from math import floor, sqrt
from typing import List

def factorize(input_val: int) -> List[int]:
    results: List[int] = []
    ctr: int = 2
    limit: int = floor(sqrt(input_val)) + 1
    while ctr <= limit and input_val > 1:
        if input_val % ctr == 0:
            results.append(ctr)
            input_val //= ctr
            limit = floor(sqrt(input_val)) + 1  # update limit since input_val changed
        else:
            ctr += 1
    if input_val > 1:
        results.append(input_val)
    return results