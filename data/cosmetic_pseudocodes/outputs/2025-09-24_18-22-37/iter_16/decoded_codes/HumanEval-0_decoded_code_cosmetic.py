from typing import Sequence


def has_close_elements(numbers_array: Sequence[float], delta_limit: float) -> bool:
    outer_idx: int = 0
    length: int = len(numbers_array)
    while outer_idx < length:
        first_val: float = numbers_array[outer_idx]
        inner_idx: int = 0
        while inner_idx < length:
            if outer_idx != inner_idx:
                second_val: float = numbers_array[inner_idx]
                diff_calc: float = first_val - second_val
                abs_diff: float = diff_calc if diff_calc >= 0 else -diff_calc
                if abs_diff < delta_limit:
                    return True
            inner_idx += 1
        outer_idx += 1
    return False