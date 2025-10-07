from math import sqrt
from typing import List

def factorize(param_x: int) -> List[int]:
    results: List[int] = []
    current_div: int = 2
    limit: int = int(sqrt(param_x)) + 1
    while current_div <= limit:
        if param_x % current_div == 0:
            results.append(current_div)
            param_x //= current_div
            limit = int(sqrt(param_x)) + 1
        else:
            current_div += 1
    if param_x > 1:
        results.append(param_x)
    return results