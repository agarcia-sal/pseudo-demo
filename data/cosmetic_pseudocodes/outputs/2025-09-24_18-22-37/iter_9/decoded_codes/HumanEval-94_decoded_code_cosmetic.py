from typing import Sequence


def skjkasdkd(series_of_ints: Sequence[int]) -> int:
    def isPrime(number_val: int) -> bool:
        if number_val < 2:
            return False
        candidate: int = 2
        upper_limit: int = int(number_val**0.5) + 1
        while candidate < upper_limit:
            if number_val % candidate == 0:
                return False
            candidate += 1
        return True

    highest_prime: int = 0
    pos: int = 0
    length: int = len(series_of_ints)
    while pos < length:
        current_num: int = series_of_ints[pos]
        if highest_prime < current_num and isPrime(current_num):
            highest_prime = current_num
        pos += 1

    digits_sum: int = sum(int(digit_char) for digit_char in str(highest_prime))
    return digits_sum