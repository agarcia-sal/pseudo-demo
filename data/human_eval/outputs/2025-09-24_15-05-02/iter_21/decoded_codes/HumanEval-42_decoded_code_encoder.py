from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_list: List[int] = []
    for element in list_of_elements:
        incremented_element = element + 1
        result_list.append(incremented_element)
    return result_list