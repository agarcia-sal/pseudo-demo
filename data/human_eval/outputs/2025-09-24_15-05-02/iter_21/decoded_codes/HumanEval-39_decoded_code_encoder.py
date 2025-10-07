from math import isqrt
from typing import List

def prime_fib(n: int) -> int:
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        limit = min(isqrt(number) + 1, number - 1)
        for k in range(2, limit):
            if number % k == 0:
                return False
        return True

    fibonacci_list: List[int] = [0, 1]
    while True:
        next_fib = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fib)
        if is_prime(next_fib):
            n -= 1
        if n == 0:
            return next_fib