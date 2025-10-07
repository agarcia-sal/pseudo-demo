from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if len(input_list) == 0:
        return []
    initial_index_value: int = 0
    last_index_value: int = len(input_list) - 1
    first_element: int = input_list[initial_index_value]
    last_element: int = input_list[last_index_value]
    combined_sum: int = first_element + last_element
    is_even_sum: bool = (combined_sum % 2) == 0
    sorted_result: List[int] = sorted(input_list, reverse=is_even_sum)
    return sorted_result