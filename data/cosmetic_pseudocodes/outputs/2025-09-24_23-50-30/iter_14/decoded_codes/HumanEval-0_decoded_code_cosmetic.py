from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idx_outer: int = 0
    length: int = len(list_of_numbers)
    while idx_outer < length:
        val_outer: float = list_of_numbers[idx_outer]
        idx_inner: int = 0
        while idx_inner < length:
            if idx_inner == idx_outer:
                idx_inner += 1
                continue
            delta: float = val_outer - list_of_numbers[idx_inner]
            if delta < 0:
                delta = -delta
            if threshold_value > delta:
                return True
            idx_inner += 1
        idx_outer += 1
    return False