from math import sqrt, floor
from typing import List


def factorize(integer_n: int) -> List[int]:
    primes_collection: List[int] = []
    trial_divisor: int = 2

    while trial_divisor <= floor(sqrt(integer_n)) + 1:
        if integer_n % trial_divisor == 0:
            primes_collection.append(trial_divisor)
            integer_n //= trial_divisor
        else:
            trial_divisor += 1

    if integer_n > 1:
        primes_collection.append(integer_n)

    return primes_collection