from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_array: List[int] = []
    idx_counter: int = 0
    total_elems: int = len(list_of_elements)
    while not (idx_counter >= total_elems):
        current_element_value: int = list_of_elements[idx_counter]
        incremented_val: int = 1 + current_element_value
        result_array = result_array + [incremented_val]
        idx_counter += 1
    return result_array