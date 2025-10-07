from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(integer_a: int, integer_b: int) -> bool:
            if integer_b > integer_a:
                return True
            elif integer_a % integer_b == 0:
                return False
            else:
                return check_divisor(integer_a, integer_b + 1)

        return check_divisor(integer_p, 2)

    base_sequence: List[int] = [0, 1]

    def recur_loop(current_list: List[int], count: int) -> int:
        last = current_list[-1]
        second_last = current_list[-2]
        next_val = last + second_last
        new_list = current_list + [next_val]

        if is_prime(next_val):
            new_count = count - 1
        else:
            new_count = count

        if new_count != 0:
            return recur_loop(new_list, new_count)
        else:
            return next_val

    return recur_loop(base_sequence, integer_n)