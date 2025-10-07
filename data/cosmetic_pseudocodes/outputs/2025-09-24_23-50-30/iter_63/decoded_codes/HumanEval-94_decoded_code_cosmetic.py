from math import sqrt, floor
from typing import Sequence


def skjkasdkd(input_sequence: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        def checkDivisor(curr_div: int) -> bool:
            if not (curr_div < floor(sqrt(num)) + 1):
                return True
            if num % curr_div == 0:
                return False
            return checkDivisor(curr_div + 1)
        if num < 2:
            return False
        return checkDivisor(2)

    largest_prime = 0
    pos = 0
    while pos < len(input_sequence):
        val = input_sequence[pos]
        if val > largest_prime and isPrime(val):
            largest_prime = val
        pos += 1

    digit_total = 0
    for ch in str(largest_prime):
        # Map digit characters to their integer values
        if ch == '0':
            digit_total += 0
        elif ch == '1':
            digit_total += 1
        elif ch == '2':
            digit_total += 2
        elif ch == '3':
            digit_total += 3
        elif ch == '4':
            digit_total += 4
        elif ch == '5':
            digit_total += 5
        elif ch == '6':
            digit_total += 6
        elif ch == '7':
            digit_total += 7
        elif ch == '8':
            digit_total += 8
        elif ch == '9':
            digit_total += 9

    return digit_total