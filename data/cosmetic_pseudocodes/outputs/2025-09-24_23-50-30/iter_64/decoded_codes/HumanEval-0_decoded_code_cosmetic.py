from typing import Sequence

def has_close_elements(arg_alpha: Sequence[float], arg_beta: float) -> bool:
    idx_a = 0
    length = len(arg_alpha)
    while idx_a < length:
        idx_b = 0
        while idx_b < length:
            if idx_a != idx_b:
                val_diff = arg_alpha[idx_a] - arg_alpha[idx_b]
                if val_diff < 0:
                    val_diff = -val_diff
                if val_diff < arg_beta:
                    return True
            idx_b += 1
        idx_a += 1
    return False