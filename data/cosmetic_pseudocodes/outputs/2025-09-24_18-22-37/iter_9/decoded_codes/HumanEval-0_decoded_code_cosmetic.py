from typing import Sequence

def has_close_elements(array_input: Sequence[int], limit_param: int) -> bool:
    idx_i: int = 0
    length: int = len(array_input)
    while idx_i < length:
        val_a: int = array_input[idx_i]
        idx_j: int = 0
        while idx_j < length:
            val_b: int = array_input[idx_j]
            if idx_i != idx_j:
                diff_temp: int = val_a - val_b
                diff_abs: int = diff_temp if diff_temp >= 0 else -diff_temp
                if diff_abs < limit_param:
                    return True
            idx_j += 1
        idx_i += 1
    return False