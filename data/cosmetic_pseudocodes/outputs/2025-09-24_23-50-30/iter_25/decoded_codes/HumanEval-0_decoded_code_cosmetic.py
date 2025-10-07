from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_index = 0
    length = len(list_of_numbers)
    while outer_index < length:
        current_outer = list_of_numbers[outer_index]
        inner_index = 0
        while inner_index < length:
            if outer_index != inner_index:
                diff_abs = current_outer - list_of_numbers[inner_index]
                if diff_abs < 0:
                    diff_abs = -diff_abs
                if diff_abs < threshold_value:
                    return True
            inner_index += 1
        outer_index += 1
    return False