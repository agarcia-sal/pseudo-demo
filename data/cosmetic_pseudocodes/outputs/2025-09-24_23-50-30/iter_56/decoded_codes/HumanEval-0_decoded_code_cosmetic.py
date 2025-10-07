from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length_numbers = len(list_of_numbers)
    outer_index = 0

    while outer_index < length_numbers:
        inner_index = 0
        while inner_index < length_numbers:
            if outer_index != inner_index:
                diff_val = abs(list_of_numbers[outer_index] - list_of_numbers[inner_index])
                if diff_val < threshold_value:
                    return True
            inner_index += 1
        outer_index += 1

    return False