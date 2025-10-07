from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False
        limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)

        def check_divisor(integer_y: int, integer_limit: int) -> bool:
            if integer_y > integer_limit:
                return True
            if integer_p % integer_y == 0:
                return False
            return check_divisor(integer_y + 1, integer_limit)

        return check_divisor(2, limit)

    sequence_fibs: List[int] = [0, 1]

    def find_nth_prime_fib(remaining_counter: int, fibs_list: List[int]) -> int:
        next_val = fibs_list[-2] + fibs_list[-1]
        updated_list = fibs_list + [next_val]
        updated_counter = remaining_counter
        if is_prime(next_val):
            updated_counter -= 1
        if updated_counter == 0:
            return next_val
        return find_nth_prime_fib(updated_counter, updated_list)

    return find_nth_prime_fib(integer_n, sequence_fibs)