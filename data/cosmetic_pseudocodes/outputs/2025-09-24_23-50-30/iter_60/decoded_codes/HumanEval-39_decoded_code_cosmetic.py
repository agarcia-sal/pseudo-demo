from math import floor, sqrt
from typing import List


def prime_fib(arg_num: int) -> int:
    def is_prime(inner_val: int) -> bool:
        if inner_val < 2:
            return False

        def search_divisor(depth_itor: int) -> bool:
            limit = min(floor(sqrt(inner_val)) + 1, inner_val - 1)
            if depth_itor > limit:
                return True
            if inner_val % depth_itor == 0:
                return False
            return search_divisor(depth_itor + 1)

        return search_divisor(2)

    fib_seq: List[int] = [0, 1]

    def loop_process(count_rem: int) -> int:
        def add_next() -> int:
            next_val = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_val)
            return next_val

        current = add_next()
        if is_prime(current):
            count_rem -= 1
            if count_rem == 0:
                return current
        return loop_process(count_rem)

    return loop_process(arg_num)