from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def check_divisor(integer_q: int, integer_limit: int) -> bool:
            if integer_q > integer_limit:
                return True
            elif integer_p % integer_q == 0:
                return False
            else:
                return check_divisor(integer_q + 1, integer_limit)

        if integer_p < 2:
            return False
        sqrt_limit = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        return check_divisor(2, sqrt_limit)

    def add_next_fib(seq_accum: List[int]) -> List[int]:
        def sum_last_two(lst: List[int]) -> int:
            return lst[-1] + lst[-2]

        return seq_accum + [sum_last_two(seq_accum)]

    def prime_fib_recursive(prime_count: int, fib_sequence: List[int]) -> int:
        if prime_count == 0:
            return fib_sequence[-1]
        updated_seq = add_next_fib(fib_sequence)
        last_val = updated_seq[-1]
        new_prime_count = prime_count - (1 if is_prime(last_val) else 0)
        return prime_fib_recursive(new_prime_count, updated_seq)

    return prime_fib_recursive(integer_n, [0, 1])