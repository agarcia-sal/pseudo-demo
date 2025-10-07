from math import sqrt, floor
from typing import List


def factorize(integer_n: int) -> List[int]:
    primes: List[int] = []
    current_divisor = 2
    limit = floor(sqrt(integer_n)) + 1

    while current_divisor <= limit:
        if integer_n % current_divisor == 0:
            primes.append(current_divisor)
            integer_n //= current_divisor
            limit = floor(sqrt(integer_n)) + 1
        else:
            current_divisor += 1

    if integer_n > 1:
        primes.append(integer_n)

    return primes