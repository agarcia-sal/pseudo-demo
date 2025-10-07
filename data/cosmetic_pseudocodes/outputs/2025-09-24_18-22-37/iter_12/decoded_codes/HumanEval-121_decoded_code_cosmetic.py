from typing import List

def solution(array_of_numbers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0
    while position < len(array_of_numbers):
        current_element: int = array_of_numbers[position]
        is_index_even: bool = (position % 2) == 0
        is_element_odd: bool = (current_element % 2) == 1
        if is_index_even:
            if is_element_odd:
                total_sum += current_element
        position += 1
    return total_sum