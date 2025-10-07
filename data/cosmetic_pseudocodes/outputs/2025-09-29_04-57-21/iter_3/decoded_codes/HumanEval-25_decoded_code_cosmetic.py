from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []

    def helper(divider: int) -> None:
        nonlocal integer_n
        if divider > int(sqrt(integer_n)) + 1:
            return
        if integer_n % divider == 0:
            factors.append(divider)
            integer_n //= divider
            helper(divider)
        else:
            helper(divider + 1)

    helper(2)
    if integer_n > 1:
        factors.append(integer_n)
    return factors