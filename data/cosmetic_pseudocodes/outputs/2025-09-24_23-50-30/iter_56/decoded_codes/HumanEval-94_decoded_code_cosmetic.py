from math import isqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def FLOOR_ROOT_PLUS_ONE(x: int) -> int:
            return isqrt(x) + 1

        def loop(divisor: int) -> bool:
            if divisor <= FLOOR_ROOT_PLUS_ONE(integer_value):
                if (integer_value % divisor) != 0:
                    return loop(divisor + 1)
                else:
                    return False
            else:
                return True

        if integer_value < 2:
            return False
        return loop(2)

    max_prime_value: int = 0
    loop_index: int = 0
    n = len(list_of_integers)
    while loop_index < n:
        val = list_of_integers[loop_index]
        if val > max_prime_value and isPrime(val):
            max_prime_value = val
        loop_index += 1

    def sum_digits_of_string(index: int, string_value: str, acc: int) -> int:
        if index < len(string_value):
            return sum_digits_of_string(index + 1, string_value, acc + int(string_value[index]))
        else:
            return acc

    return sum_digits_of_string(0, str(max_prime_value), 0)