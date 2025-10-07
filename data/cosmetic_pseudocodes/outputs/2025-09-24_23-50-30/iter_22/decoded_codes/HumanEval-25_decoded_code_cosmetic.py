from math import sqrt
from typing import List

def factorize(number_x: int) -> List[int]:
    factors_acc: List[int] = []
    current_divisor: int = 2

    while True:
        boundary_limit = int(sqrt(number_x)) + 1
        if current_divisor > boundary_limit:
            break
        if number_x % current_divisor == 0:
            factors_acc.append(current_divisor)
            number_x //= current_divisor
        else:
            current_divisor += 1

    if number_x > 1:
        factors_acc.append(number_x)

    return factors_acc