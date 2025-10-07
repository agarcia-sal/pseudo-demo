from typing import Sequence

def solution(nums_collection: Sequence[int]) -> int:
    total_sum: int = 0
    index_counter: int = 0
    length: int = len(nums_collection)
    while True:
        if index_counter >= length:
            break
        current_element: int = nums_collection[index_counter]
        is_index_even: bool = (index_counter % 2) == 0
        is_element_odd: bool = (current_element % 2) == 1
        if is_index_even and is_element_odd:
            total_sum += current_element
        index_counter += 1
    return total_sum