from math import sqrt
from typing import List


def prime_fib(input_number: int) -> int:
    def is_prime(test_value: int) -> bool:
        if test_value < 2:
            return False

        def check_divisor(divisor: int) -> bool:
            limit = int(sqrt(test_value)) + 1
            if divisor > limit or divisor >= test_value:
                return True
            if test_value % divisor == 0:
                return False
            return check_divisor(divisor + 1)

        return check_divisor(2)

    sequence: List[int] = [0, 1]

    def find_prime_fib(counter: int) -> int:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
        if is_prime(next_value):
            counter -= 1
            if counter == 0:
                return next_value
        return find_prime_fib(counter)

    return find_prime_fib(input_number)