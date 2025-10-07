from typing import Sequence

def mean_absolute_deviation(array_b: Sequence[float]) -> float:
    count_c: int = len(array_b)
    if count_c == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    sum_d: float = 0
    for index_e in range(count_c):
        sum_d += array_b[index_e]
    avg_f: float = sum_d / count_c

    abs_sum_g: float = 0
    for i_h in range(count_c):
        diff_i: float = array_b[i_h] - avg_f
        abs_diff_j: float = abs(diff_i)
        abs_sum_g += abs_diff_j

    mad_k: float = abs_sum_g / count_c
    return mad_k