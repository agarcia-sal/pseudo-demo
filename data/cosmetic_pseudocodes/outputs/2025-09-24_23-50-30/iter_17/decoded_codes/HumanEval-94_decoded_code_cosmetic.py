from math import floor, exp, log
from typing import Collection


def skjkasdkd(almost_any_collection: Collection[int]) -> int:
    def isPrime(some_integer: int) -> bool:
        if some_integer < 2:
            return False
        limit = 1 + floor(exp(0.5 * log(some_integer)))
        seed = 2
        while seed <= limit:
            if some_integer % seed == 0:
                return False
            seed += 1
        return True

    highest_prime = 0
    pointer = 0
    size = len(almost_any_collection)
    # to allow indexing like pseudocode, convert to list if not already
    if not isinstance(almost_any_collection, list):
        almost_any_collection = list(almost_any_collection)

    while pointer < size:
        value = almost_any_collection[pointer]
        if isPrime(value) and (highest_prime < value):
            highest_prime = value
        pointer += 1

    sum_accumulator = 0
    for digit in str(highest_prime):
        sum_accumulator += int(digit)

    return sum_accumulator