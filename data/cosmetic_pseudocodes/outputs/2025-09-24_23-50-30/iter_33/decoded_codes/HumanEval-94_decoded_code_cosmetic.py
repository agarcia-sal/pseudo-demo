from math import floor, sqrt
from typing import Iterable

def skjkasdkd(collection_of_numbers: Iterable[int]) -> int:
    def isPrime(check_num: int) -> bool:
        if check_num < 2:
            return False
        candidate = 2
        boundary = 1 + floor(sqrt(check_num))
        while candidate <= boundary:
            if check_num % candidate == 0:
                return False
            candidate += 1
        return True

    accumulator = 0
    position = 0
    seq = list(collection_of_numbers)  # Ensure indexable
    while position < len(seq):
        if seq[position] > accumulator and isPrime(seq[position]):
            accumulator = seq[position]
        position += 1

    digit_sum = sum(int(char) for char in str(accumulator))
    return digit_sum