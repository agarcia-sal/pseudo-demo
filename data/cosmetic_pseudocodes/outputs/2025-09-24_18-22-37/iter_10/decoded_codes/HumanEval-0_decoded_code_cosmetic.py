from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_counter = 0
    length = len(list_of_numbers)
    while outer_counter < length:
        outer_item = list_of_numbers[outer_counter]
        inner_counter = 0
        while inner_counter < length:
            if outer_counter != inner_counter:
                inner_item = list_of_numbers[inner_counter]
                temp_diff = outer_item - inner_item
                if temp_diff < 0:
                    temp_diff = -temp_diff
                if temp_diff < threshold_value:
                    return True
            inner_counter += 1
        outer_counter += 1
    return False