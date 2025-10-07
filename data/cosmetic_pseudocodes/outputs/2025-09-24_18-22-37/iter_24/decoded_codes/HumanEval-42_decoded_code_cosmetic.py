from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    updated_list: List[int] = []
    idx: int = 0
    while idx < len(list_of_elements):
        current_item: int = list_of_elements[idx]
        incremented_val: int = current_item + 1
        updated_list.append(incremented_val)
        idx += 1
    return updated_list