from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    new_list: List[int] = []
    idx: int = 0
    while idx < len(list_of_elements):
        incremented_element: int = list_of_elements[idx] + 1
        new_list.append(incremented_element)
        idx += 1
    return new_list