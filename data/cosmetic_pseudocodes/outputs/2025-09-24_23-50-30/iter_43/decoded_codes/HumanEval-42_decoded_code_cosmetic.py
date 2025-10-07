from typing import List

def incr_list(array_items: List[int]) -> List[int]:
    result_array: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_items):
        result_array.append(array_items[index_counter] + 1)
        index_counter += 1
    return result_array