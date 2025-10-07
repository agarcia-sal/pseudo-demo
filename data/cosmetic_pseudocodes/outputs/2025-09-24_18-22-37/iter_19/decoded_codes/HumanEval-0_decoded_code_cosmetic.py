from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_idx: int = 0
    length: int = len(list_of_numbers)
    while outer_idx < length:
        outer_val: float = list_of_numbers[outer_idx]
        inner_idx: int = 0
        while True:
            if inner_idx >= length:
                break
            inner_val: float = list_of_numbers[inner_idx]
            if outer_idx != inner_idx:
                diff_tmp: float = outer_val - inner_val
                if diff_tmp < 0:
                    diff_tmp = -diff_tmp
                if diff_tmp < threshold_value:
                    return True
            inner_idx += 1
        outer_idx += 1
    return False