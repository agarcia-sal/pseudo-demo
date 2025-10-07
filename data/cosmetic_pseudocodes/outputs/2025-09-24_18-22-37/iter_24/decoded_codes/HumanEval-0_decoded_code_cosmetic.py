from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    is_found: bool = False
    outer_counter: int = 0
    n: int = len(list_of_numbers)
    while outer_counter < n:
        outer_value: float = list_of_numbers[outer_counter]
        inner_counter: int = 0
        while inner_counter < n:
            inner_value: float = list_of_numbers[inner_counter]
            condition_flag: bool = outer_counter != inner_counter
            if condition_flag:
                temp_diff: float = outer_value - inner_value
                if temp_diff < 0:
                    temp_diff = -temp_diff
                threshold_check: bool = temp_diff < threshold_value
                if threshold_check:
                    is_found = True
                    break
            inner_counter += 1
        if is_found:
            break
        outer_counter += 1
    return is_found