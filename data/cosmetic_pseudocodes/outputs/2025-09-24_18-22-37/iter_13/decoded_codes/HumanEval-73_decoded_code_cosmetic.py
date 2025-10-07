from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    result: int = 0
    total_elements: int = len(array_of_integers)
    midpoint: int = (total_elements >> 1) - 1
    cursor: int = 0
    while cursor <= midpoint:
        left_element: int = array_of_integers[cursor]
        right_index: int = total_elements - cursor - 1
        right_element: int = array_of_integers[right_index]
        if left_element != right_element:
            result += 1
        cursor += 1
    return result