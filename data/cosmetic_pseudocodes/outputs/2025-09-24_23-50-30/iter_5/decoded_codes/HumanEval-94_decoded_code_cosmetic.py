from math import isqrt
from typing import Iterable

def skjkasdkd(input_collection: Iterable[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = isqrt(num) + 1
        return all(num % divisor != 0 for divisor in range(2, limit))

    record_max_prime = 0
    position = 0
    input_list = list(input_collection)  # to support len() and indexing if input_collection is not a sequence
    length = len(input_list)

    while position != length:
        candidate = input_list[position]
        if candidate > record_max_prime:
            if isPrime(candidate):
                record_max_prime = candidate
        position += 1

    accumulator = sum(int(char) for char in str(record_max_prime))
    return accumulator