from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit_end = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        counter_k = 2
        while counter_k <= limit_end:
            if integer_p % counter_k == 0:
                return False
            counter_k += 1
        return True

    fibonacci_list: List[int] = [0, 1]

    while True:
        last_idx = len(fibonacci_list) - 1
        next_value = fibonacci_list[last_idx] + fibonacci_list[last_idx - 1]
        fibonacci_list.append(next_value)

        if is_prime(fibonacci_list[-1]):
            integer_n -= 1

        if integer_n == 0:
            return fibonacci_list[-1]