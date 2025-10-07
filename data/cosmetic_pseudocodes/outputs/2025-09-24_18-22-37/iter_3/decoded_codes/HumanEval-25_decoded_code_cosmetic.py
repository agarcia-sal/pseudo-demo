import math
from typing import List, Tuple


def factorize(integer_n: int) -> List[int]:
    factors_list: List[int] = []
    divisor: int = 2
    limit: int = math.isqrt(integer_n) + 1

    def loop_division(divisor: int, integer_n: int) -> Tuple[List[int], int]:
        if divisor > limit:
            return factors_list, integer_n
        if integer_n % divisor == 0:
            factors_list.append(divisor)
            integer_n //= divisor
            return loop_division(divisor, integer_n)
        return loop_division(divisor + 1, integer_n)

    _, integer_n = loop_division(divisor, integer_n)

    if integer_n > 1:
        factors_list.append(integer_n)

    return factors_list