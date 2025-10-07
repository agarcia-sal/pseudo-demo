from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idx_outer: int = 0
    length: int = len(list_of_numbers)
    while idx_outer < length:
        val_outer: float = list_of_numbers[idx_outer]
        idx_inner: int = 0
        while idx_inner < length:
            if idx_outer == idx_inner:
                idx_inner += 1
                continue
            val_inner: float = list_of_numbers[idx_inner]
            diff_calc: float = val_outer - val_inner
            abs_diff: float = diff_calc if diff_calc >= 0 else -diff_calc
            if abs_diff < threshold_value:
                return True
            idx_inner += 1
        idx_outer += 1
    return False