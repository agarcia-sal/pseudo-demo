from math import sqrt, floor
from typing import List


def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    root_limit: int = floor(sqrt(integer_n)) + 1

    def recurseFactor(divisor_j: int, current_n: int) -> None:
        if divisor_j > root_limit:
            if current_n > 1:
                factors.append(current_n)
            return

        if current_n % divisor_j != 0:
            recurseFactor(divisor_j + 1, current_n)
            return

        factors.append(divisor_j)
        updated_n = current_n // divisor_j
        recurseFactor(divisor_j, updated_n)

    recurseFactor(2, integer_n)
    return factors