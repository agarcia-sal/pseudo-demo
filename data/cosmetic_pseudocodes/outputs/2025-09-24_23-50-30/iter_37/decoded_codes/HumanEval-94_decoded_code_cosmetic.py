from math import isqrt
from typing import Sequence


def skjkasdkd(seq_of_nums: Sequence[int]) -> int:
    def isPrime(val: int) -> bool:
        if val < 2:
            return False
        for test_divisor in range(2, isqrt(val) + 2):
            if val % test_divisor == 0:
                return False
        return True

    peak_prime: int = 0
    pos: int = 0
    length: int = len(seq_of_nums)
    while pos < length:
        val = seq_of_nums[pos]
        if val > peak_prime and isPrime(val):
            peak_prime = val
        pos += 1

    digit_sum: int = sum(int(ch) for ch in str(peak_prime))
    return digit_sum