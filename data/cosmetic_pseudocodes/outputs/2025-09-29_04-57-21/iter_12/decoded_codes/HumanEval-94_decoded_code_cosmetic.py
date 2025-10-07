from math import isqrt
from typing import Iterable

def skjkasdkd(collection_of_numbers: Iterable[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        boundary: int = isqrt(num) + 1
        candidate: int = 2
        while candidate < boundary:
            if num % candidate == 0:
                return False
            candidate += 1
        return True

    highest_prime: int = 0
    pos: int = 0
    collection_list = list(collection_of_numbers)  # Support multiple passes and indexing
    length: int = len(collection_list)
    while pos < length:
        val = collection_list[pos]
        if val > highest_prime and isPrime(val):
            highest_prime = val
        pos += 1

    total_digits: int = 0
    digits: str = str(highest_prime)
    digit_index: int = 0
    length_digits: int = len(digits)
    while digit_index < length_digits:
        total_digits += int(digits[digit_index])
        digit_index += 1

    return total_digits