from typing import List

def f(param_n: int) -> List[int]:
    list_accum: List[int] = []
    idx_outer: int = 1
    while idx_outer <= param_n:
        if idx_outer % 2 != 0:
            sum_accum: int = 0
            idx_inner: int = 1
            while idx_inner <= idx_outer:
                sum_accum += idx_inner
                idx_inner += 1
            list_accum.append(sum_accum)
            idx_outer += 1
            continue
        prod_accum: int = 1
        idx_inner: int = 1
        while idx_inner <= idx_outer:
            prod_accum *= idx_inner
            idx_inner += 1
        list_accum.append(prod_accum)
        idx_outer += 1
    return list_accum