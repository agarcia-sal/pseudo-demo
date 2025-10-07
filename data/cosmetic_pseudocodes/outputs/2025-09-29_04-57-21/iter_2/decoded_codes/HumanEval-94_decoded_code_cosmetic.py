from math import sqrt, floor
from typing import Sequence

def skjkasdkd(number_sequence: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = floor(sqrt(num)) + 1
        candidate = 2
        while candidate <= limit:
            if num % candidate == 0:
                return False
            candidate += 1
        return True

    highest_prime = 0
    for num in number_sequence:
        if num > highest_prime and isPrime(num):
            highest_prime = num

    return sum(int(d) for d in str(highest_prime))