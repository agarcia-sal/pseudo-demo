import math
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(int(math.isqrt(integer_p)) + 1, integer_p - 1)
        for j in range(2, limit + 1):
            if integer_p % j == 0:
                return False
        return True

    list_fibonacci: List[int] = [0, 1]

    while True:
        last_index: int = len(list_fibonacci) - 1
        second_last_index: int = last_index - 1
        new_fib: int = list_fibonacci[last_index] + list_fibonacci[second_last_index]
        list_fibonacci.append(new_fib)

        if is_prime(list_fibonacci[-1]):
            integer_n -= 1

        if integer_n == 0:
            return list_fibonacci[-1]