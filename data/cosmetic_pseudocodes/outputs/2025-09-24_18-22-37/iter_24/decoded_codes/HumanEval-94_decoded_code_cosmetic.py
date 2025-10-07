from math import isqrt
from typing import List

def skjkasdkd(bag_of_numbers: List[int]) -> int:
    def isPrime(v: int) -> bool:
        if v < 2:
            return False
        root_bound: int = isqrt(v) + 1
        amt: int = 2
        while amt < root_bound:
            if v % amt == 0:
                return False
            amt += 1
        return True

    highest_prime: int = 0
    pos: int = 0
    while pos < len(bag_of_numbers):
        candidate: int = bag_of_numbers[pos]
        if candidate > highest_prime and isPrime(candidate):
            highest_prime = candidate
        pos += 1

    digit_sum: int = 0
    digits_str: str = str(highest_prime)
    idx: int = 0
    while idx < len(digits_str):
        ch: str = digits_str[idx]
        digit_sum += int(ch)
        idx += 1

    return digit_sum