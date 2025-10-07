from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for outer_index in range(len(list_of_numbers)):
        primary_element = list_of_numbers[outer_index]
        for inner_index in range(len(list_of_numbers)):
            if inner_index != outer_index:
                gap = abs(primary_element - list_of_numbers[inner_index])
                if gap < threshold_value:
                    return True
    return False