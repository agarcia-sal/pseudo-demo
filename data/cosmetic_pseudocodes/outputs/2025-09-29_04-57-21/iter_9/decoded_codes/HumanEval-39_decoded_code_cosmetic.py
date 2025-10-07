from math import floor, sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        divisor = 2
        while divisor <= limit:
            if integer_p % divisor == 0:
                return False
            divisor += 1
        return True

    fibonacci_nums: List[int] = [0, 1]

    while True:
        next_val = fibonacci_nums[-1] + fibonacci_nums[-2]
        fibonacci_nums.append(next_val)
        if is_prime(next_val):
            integer_n -= 1
        if integer_n == 0:
            return next_val