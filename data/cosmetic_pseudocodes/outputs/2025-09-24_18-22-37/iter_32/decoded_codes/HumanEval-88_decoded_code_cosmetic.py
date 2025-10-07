from typing import List

def sort_array(array: List[int]) -> List[int]:
    size_indicator: int = len(array)
    if size_indicator == 0:
        return []
    start_element: int = array[0]
    last_element_index: int = size_indicator - (1 + 0)
    end_element: int = array[last_element_index]
    total_sum: int = start_element + end_element
    evenness_flag: bool = (total_sum % 2) == 0
    sorted_result: List[int] = sorted(array)
    if evenness_flag:
        return sorted_result[::-1]  # descending order
    else:
        return sorted_result      # ascending order