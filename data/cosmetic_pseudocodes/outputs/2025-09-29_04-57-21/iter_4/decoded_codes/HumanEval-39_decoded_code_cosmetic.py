from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(integer_p - 1, floor(sqrt(integer_p)) + 1)
        for i in range(2, limit + 1):
            if integer_p % i == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        last_index = len(list_fibonacci) - 1
        new_fib_number = list_fibonacci[last_index] + list_fibonacci[last_index - 1]
        list_fibonacci.append(new_fib_number)

        if is_prime(new_fib_number):
            integer_n -= 1

        if integer_n == 0:
            return new_fib_number