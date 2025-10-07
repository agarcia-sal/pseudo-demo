from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idx_outer = 0
    length = len(list_of_numbers)
    while idx_outer < length:
        idx_inner = 0
        while idx_inner < length:
            if idx_inner != idx_outer:
                delta = list_of_numbers[idx_outer] - list_of_numbers[idx_inner]
                abs_delta = delta if delta >= 0 else -delta
                if abs_delta < threshold_value:
                    return True
            idx_inner += 1
        idx_outer += 1
    return False