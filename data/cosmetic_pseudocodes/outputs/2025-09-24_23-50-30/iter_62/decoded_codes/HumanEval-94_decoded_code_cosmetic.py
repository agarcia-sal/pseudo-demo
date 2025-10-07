from math import sqrt
from typing import List


def skjkasdkd(array_input: List[int]) -> int:
    def isPrime(number_param: int) -> bool:
        def checkDivisor(current_divisor: int, limit_divisor: int) -> bool:
            if current_divisor > limit_divisor:
                return True
            if number_param % current_divisor == 0:
                return False
            return checkDivisor(current_divisor + 1, limit_divisor)

        if number_param < 2:
            return False
        return checkDivisor(2, int(sqrt(number_param)) + 1)

    highest_prime: int = 0
    position_counter: int = 0
    length: int = len(array_input)

    while position_counter < length:
        val = array_input[position_counter]
        if val > highest_prime and isPrime(val):
            highest_prime = val
        position_counter += 1

    def sumDigits(digit_chars: str, accumulator: int) -> int:
        if not digit_chars:
            return accumulator
        return sumDigits(digit_chars[1:], accumulator + int(digit_chars[0]))

    return sumDigits(str(highest_prime), 0)