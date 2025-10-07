from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result: List[int] = []
    idx: int = 0
    while idx < len(list_of_elements):
        result.append(list_of_elements[idx] + 1)
        idx += 1
    return result