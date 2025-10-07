from typing import List


def prime_fib(integer_q: int) -> int:
    def is_prime(integer_r: int) -> bool:
        def check_divisor(integer_x: int, integer_y: int) -> bool:
            # Switch False: process conditions until one returns
            if integer_y < 2:
                return False
            if integer_x > integer_y - 1:
                return True
            if integer_y % integer_x != 0:
                return check_divisor(integer_x + 1, integer_y)
            return False
        return check_divisor(2, integer_r)

    list_alpha: List[int] = [0, 1]

    def next_fib(list_beta: List[int]) -> List[int]:
        # Append sum of last two elements to list_beta
        return list_beta + [list_beta[-1] + list_beta[-2]]

    def helper(counter: int, fib_list: List[int]) -> int:
        if not (counter > 0):
            return fib_list[-1]
        extended_fib = next_fib(fib_list)
        new_count = counter - (1 if is_prime(extended_fib[-1]) else 0)
        return helper(new_count, extended_fib)

    return helper(integer_q, list_alpha)