from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idx_A: int = 0
    length: int = len(list_of_numbers)
    while idx_A < length:
        val_A: float = list_of_numbers[idx_A]
        idx_B: int = 0
        while idx_B < length:
            val_B: float = list_of_numbers[idx_B]
            if idx_A != idx_B:
                diff_temp: float = val_A - val_B
                if diff_temp < 0:
                    diff_temp = -diff_temp
                if diff_temp < threshold_value:
                    return True
            idx_B += 1
        idx_A += 1
    return False