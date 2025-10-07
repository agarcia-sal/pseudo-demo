from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def check_factor(current_val: int, upper_limit: int, prime_flag: bool) -> bool:
            if current_val >= upper_limit:
                return prime_flag
            prime_flag_updated = prime_flag and (integer_p % current_val != 0)
            return check_factor(current_val + 1, upper_limit, prime_flag_updated)

        if integer_p < 2:
            return False
        limit_val = min(int(sqrt(integer_p)) + 1, integer_p - 1)
        return check_factor(2, limit_val, True)

    def add_last_two(lst: List[int]) -> int:
        size_lst = len(lst)
        return lst[size_lst - 1] + lst[size_lst - 2]

    FIB_SEQ: List[int] = [0, 1]

    def iterate_fib(prime_counter: int, fib_sequence: List[int]) -> int:
        prime_goal = prime_counter
        current_sequence = fib_sequence
        if prime_goal == 0:
            return current_sequence[len(current_sequence) - 1]
        next_fib = add_last_two(current_sequence)
        updated_sequence = current_sequence + [next_fib]
        is_prime_flag = is_prime(next_fib)
        new_goal = prime_goal - (1 if is_prime_flag else 0)
        return iterate_fib(new_goal, updated_sequence)

    return iterate_fib(integer_n, FIB_SEQ)