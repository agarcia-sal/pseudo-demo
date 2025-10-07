from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_list: List[int] = []
    index: int = 0
    while index < len(list_of_elements):
        result_list.append(list_of_elements[index] + 1)
        index += 1
    return result_list