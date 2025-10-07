from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idx_primary: int = 0
    length: int = len(list_of_numbers)
    while idx_primary < length:
        val_primary: float = list_of_numbers[idx_primary]
        idx_secondary: int = 0
        while idx_secondary < length:
            val_secondary: float = list_of_numbers[idx_secondary]
            if idx_primary != idx_secondary:
                temp_diff: float = val_primary - val_secondary
                if temp_diff < 0:
                    temp_diff = -temp_diff
                if temp_diff < threshold_value:
                    return True
            idx_secondary += 1
        idx_primary += 1
    return False