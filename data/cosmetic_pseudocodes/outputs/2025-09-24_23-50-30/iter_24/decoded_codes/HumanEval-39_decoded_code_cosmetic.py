from math import isqrt
from typing import List


def prime_fib(quant_x: int) -> int:
    def is_prime(test_m: int) -> bool:
        if test_m < 2:
            return False
        arr_iter: List[int] = []
        idx_s: int = 2
        limit_u: int = isqrt(test_m) + 1
        high_a: int = test_m - 1
        limit_v: int = limit_u if high_a >= limit_u else high_a

        while idx_s <= limit_v:
            arr_iter.append(idx_s)
            idx_s += 1

        def check_division(pos: int) -> bool:
            if pos >= len(arr_iter):
                return True
            elif test_m % arr_iter[pos] == 0:
                return False
            else:
                return check_division(pos + 1)

        return check_division(0)

    seq_nums: List[int] = [0, 1]

    def continue_search(flag_y: int) -> int:
        len_arr: int = len(seq_nums)
        elem_n: int = seq_nums[len_arr - 1]
        elem_o: int = seq_nums[len_arr - 2]
        seq_nums.append(elem_o + elem_n)
        if is_prime(seq_nums[-1]):
            flag_y -= 1
        if flag_y == 0:
            return seq_nums[-1]
        else:
            return continue_search(flag_y)

    return continue_search(quant_x)