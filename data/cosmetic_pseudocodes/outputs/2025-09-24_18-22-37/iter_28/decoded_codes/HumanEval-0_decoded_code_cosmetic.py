from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    flag_found: bool = False
    outer_index: int = 0
    length: int = len(list_of_numbers)
    while outer_index < length:
        current_element: float = list_of_numbers[outer_index]
        inner_index: int = 0
        while inner_index < length and not flag_found:
            if outer_index != inner_index:
                comparison_element: float = list_of_numbers[inner_index]
                temp_diff: float = abs(current_element - comparison_element)
                if temp_diff < threshold_value:
                    flag_found = True
            inner_index += 1
        if flag_found:
            return True
        outer_index += 1
    return False