from math import sqrt, floor
from typing import Sequence

def skjkasdkd(sequence: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = floor(sqrt(num)) + 1
        candidate = 2
        while candidate < limit:
            if num % candidate == 0:
                return False
            candidate += 1
        return True

    greatest_prime = 0
    for idx in range(len(sequence)):
        val = sequence[idx]
        if val > greatest_prime and isPrime(val):
            greatest_prime = val

    total_digits = sum(int(ch) for ch in str(greatest_prime))
    return total_digits