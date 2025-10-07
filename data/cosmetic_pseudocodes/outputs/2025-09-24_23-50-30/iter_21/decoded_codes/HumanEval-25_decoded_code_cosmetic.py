from math import sqrt, floor
from typing import List

def factorize(param_x: int) -> List[int]:
    factors: List[int] = []
    candidate: int = 2
    limit: int = floor(sqrt(param_x)) + 1

    def proceed_division(num: int, div: int, acc: List[int]) -> List[int]:
        if div > limit:
            return acc + [num] if num > 1 else acc
        if num % div != 0:
            return proceed_division(num, div + 1, acc)
        else:
            return proceed_division(num // div, div, acc + [div])

    return proceed_division(param_x, candidate, factors)