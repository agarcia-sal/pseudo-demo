from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors_accumulator: List[int] = []
    for current_divisor in range(2, int(sqrt(integer_n)) + 1):
        while integer_n % current_divisor == 0:
            factors_accumulator.append(current_divisor)
            integer_n //= current_divisor
    if integer_n > 1:
        factors_accumulator.append(integer_n)
    return factors_accumulator