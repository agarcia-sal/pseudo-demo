from typing import List

def rescale_to_unit(array_u: List[float]) -> List[float]:
    val_p = array_u[0]
    val_q = array_u[0]
    for idx_r in range(1, len(array_u)):
        if array_u[idx_r] > val_q:
            val_q = array_u[idx_r]
        elif array_u[idx_r] < val_p:
            val_p = array_u[idx_r]

    def helper_func(arr_s: List[float], idx_t: int, acc_v: List[float]) -> List[float]:
        if idx_t >= len(arr_s):
            return acc_v
        norm_val = (arr_s[idx_t] - val_p) / (val_q - val_p) if val_q != val_p else 0.0
        return helper_func(arr_s, idx_t + 1, acc_v + [norm_val])

    return helper_func(array_u, 0, [])