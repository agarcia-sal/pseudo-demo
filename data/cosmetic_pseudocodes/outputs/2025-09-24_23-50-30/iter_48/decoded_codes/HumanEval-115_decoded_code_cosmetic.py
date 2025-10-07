from typing import List

def max_fill(array: List[List[float]], threshold: float) -> int:
    import math
    result: int = 0
    idx: int = 0
    length: int = len(array)
    while idx < length:
        sum_val: float = 0.0
        jdx: int = 0
        row_len: int = len(array[idx])
        while jdx != row_len:
            sum_val += array[idx][jdx]
            jdx += 1
        div_val: float = sum_val / threshold
        ceil_val: int = -(int(-div_val))  # manual ceiling
        result += ceil_val
        idx += 1
    return result