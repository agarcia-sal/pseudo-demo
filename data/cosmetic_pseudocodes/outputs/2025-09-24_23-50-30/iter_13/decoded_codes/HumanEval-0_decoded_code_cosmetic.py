from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for idx_outer in range(len(list_of_numbers)):
        for idx_inner in range(len(list_of_numbers)):
            if idx_outer != idx_inner:
                diff_abs = list_of_numbers[idx_outer] + (-1 * list_of_numbers[idx_inner])
                if 0 <= diff_abs < threshold_value:
                    return True
                elif diff_abs < 0 and -diff_abs < threshold_value:
                    return True
    return False