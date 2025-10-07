from math import isqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    prime_components: List[int] = []
    potential_divisor: int = 2

    while potential_divisor <= isqrt(integer_n) + 1:
        if integer_n % potential_divisor == 0:
            prime_components.append(potential_divisor)
            integer_n //= potential_divisor
        else:
            potential_divisor += 1

    if integer_n > 1:
        prime_components.append(integer_n)

    return prime_components