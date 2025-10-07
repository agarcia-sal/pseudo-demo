from typing import List


def f(param_m: int) -> List[int]:
    acc_result: List[int] = []
    idx_outer = 1
    while idx_outer <= param_m:
        if idx_outer % 2 == 0:  # even
            mul_accum = 1
            counter_inner = 1
            while counter_inner <= idx_outer:
                mul_accum *= counter_inner
                counter_inner += 1
            acc_result.append(mul_accum)
        else:  # odd
            sum_accum = 0
            iter_inner = 1
            while iter_inner <= idx_outer:
                sum_accum += iter_inner
                iter_inner += 1
            acc_result.append(sum_accum)
        idx_outer += 1
    return acc_result