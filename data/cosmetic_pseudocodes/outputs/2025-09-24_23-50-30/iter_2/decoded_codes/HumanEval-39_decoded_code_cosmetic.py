from math import sqrt
from typing import List, Set

def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit: int = min(integer_p - 1, int(sqrt(integer_p)) + 1)
        divisors: Set[int] = set(range(limit, 1, -1))

        def check_divisor(divisors_set: Set[int]) -> bool:
            if not divisors_set:
                return True
            any_element = divisors_set.pop()
            if integer_p % any_element == 0:
                return False
            return check_divisor(divisors_set)

        return check_divisor(divisors)

    fib_seq: List[int] = [0, 1]

    def extend_and_check(k: int) -> int:
        fib_seq.append(fib_seq[k] + fib_seq[k - 1])
        nonlocal integer_n
        if integer_n > 0:
            if is_prime(fib_seq[-1]):
                integer_n -= 1
            if integer_n == 0:
                return fib_seq[-1]
            return extend_and_check(k + 1)
        # If integer_n <= 0 at start, immediately return current fib
        return fib_seq[-1]

    return extend_and_check(2)