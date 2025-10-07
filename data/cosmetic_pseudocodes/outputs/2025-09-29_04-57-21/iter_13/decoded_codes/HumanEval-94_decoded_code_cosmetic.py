from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        divisor_candidate: int = 2

        def checkDivisor() -> bool:
            nonlocal divisor_candidate
            if divisor_candidate > isqrt(integer_value):
                return True
            if integer_value % divisor_candidate == 0:
                return False
            divisor_candidate += 1
            return checkDivisor()

        if integer_value < 2:
            return False
        return checkDivisor()

    largest_prime: int = 0

    def processIndex(current_index: int) -> None:
        nonlocal largest_prime
        if current_index == len(list_of_integers):
            return
        val = list_of_integers[current_index]
        if val > largest_prime and isPrime(val):
            largest_prime = val
        processIndex(current_index + 1)

    processIndex(0)

    digits_sum: int = 0

    def accumulateDigits(digit_chars: str) -> None:
        nonlocal digits_sum
        if not digit_chars:
            return
        digits_sum += int(digit_chars[0])
        accumulateDigits(digit_chars[1:])

    accumulateDigits(str(largest_prime))

    return digits_sum