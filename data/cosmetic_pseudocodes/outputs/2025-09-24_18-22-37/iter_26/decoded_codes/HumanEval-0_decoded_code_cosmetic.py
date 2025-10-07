from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_counter: int = 0
    length: int = len(list_of_numbers)
    while outer_counter < length:
        element_a: float = list_of_numbers[outer_counter]
        inner_counter: int = 0
        while inner_counter < length:
            element_b: float = list_of_numbers[inner_counter]
            if outer_counter != inner_counter:
                temp_diff: float = element_a - element_b
                if temp_diff < 0:
                    temp_diff = -temp_diff  # absolute difference
                if temp_diff < threshold_value:
                    return True
            inner_counter += 1
        outer_counter += 1
    return False