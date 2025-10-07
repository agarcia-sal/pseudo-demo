from math import isqrt
from typing import Sequence


def skjkasdkd(seq_of_nums: Sequence[int]) -> int:
    def isPrime(num: int) -> bool:
        if num < 2:
            return False
        limit = isqrt(num) + 1
        div_iter = 2
        while div_iter < limit:
            if num % div_iter == 0:
                return False
            div_iter += 1
        return True

    greatest_prime = 0
    cursor = 0
    length = len(seq_of_nums)
    while cursor < length:
        current_val = seq_of_nums[cursor]
        if current_val > greatest_prime:
            if isPrime(current_val):
                greatest_prime = current_val
            else:
                x = 0  # placeholder as per pseudocode
        else:
            y = 0  # placeholder as per pseudocode
        cursor += 1

    total_sum = 0
    str_rep = str(greatest_prime)
    pos = 0
    length_str = len(str_rep)
    while pos < length_str:
        char_curr = str_rep[pos]
        digit_val = int(char_curr)
        total_sum += digit_val
        pos += 1

    return total_sum