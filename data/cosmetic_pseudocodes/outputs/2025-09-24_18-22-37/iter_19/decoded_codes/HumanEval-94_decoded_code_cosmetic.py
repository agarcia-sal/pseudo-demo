from math import isqrt
from typing import Sequence

def skjkasdkd(p_val: Sequence[int]) -> int:
    def isPrime(q_num: int) -> bool:
        if q_num < 2:
            return False
        i_var = 2
        while True:
            if i_var > isqrt(q_num) + 1:
                return True
            if q_num % i_var == 0:
                return False
            i_var += 1

    v_max = 0
    k_idx = 0
    while True:
        if k_idx >= len(p_val):
            break
        temp_num = p_val[k_idx]
        if temp_num > v_max and isPrime(temp_num):
            v_max = temp_num
        k_idx += 1

    sum_dgts = sum(int(ch) for ch in str(v_max))
    return sum_dgts