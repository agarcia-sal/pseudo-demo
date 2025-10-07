from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    pos_outer: int = 0
    length: int = len(list_of_numbers)
    while pos_outer < length:
        val_outer: float = list_of_numbers[pos_outer]
        pos_inner: int = 0
        while pos_inner < length:
            val_inner: float = list_of_numbers[pos_inner]
            if pos_outer != pos_inner:
                diff_calc: float = val_outer - val_inner
                abs_diff: float = diff_calc if diff_calc >= 0 else -diff_calc
                if abs_diff < threshold_value:
                    return True
            pos_inner += 1
        pos_outer += 1
    return False