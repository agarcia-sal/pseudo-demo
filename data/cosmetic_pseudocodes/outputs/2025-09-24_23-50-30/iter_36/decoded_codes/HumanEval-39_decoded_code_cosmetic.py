from math import sqrt, floor
from collections import deque
from typing import Deque

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_curr: int, integer_limit: int, boolean_flag: bool) -> bool:
            if not boolean_flag:
                return False
            if integer_curr > integer_limit:
                return True
            if integer_p % integer_curr == 0:
                return False
            return check_divisor(integer_curr + 1, integer_limit, True)

        integer_bound = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
        return check_divisor(2, integer_bound, True)

    queue_fib: Deque[int] = deque([0, 1])
    counter_n = integer_n

    def iterate_fib(queue_fib: Deque[int], counter_n: int) -> int:
        integer_a = queue_fib.popleft()
        integer_b = queue_fib[0]
        integer_sum = integer_a + integer_b
        queue_fib.append(integer_sum)

        if is_prime(integer_sum):
            counter_n -= 1

        if counter_n == 0:
            return integer_sum
        return iterate_fib(queue_fib, counter_n)

    return iterate_fib(queue_fib, counter_n)