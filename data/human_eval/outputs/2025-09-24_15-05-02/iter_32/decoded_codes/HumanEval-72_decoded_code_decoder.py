from typing import List

def will_it_fly(list_of_elements: List[int], maximum_weight: int) -> bool:
    if sum(list_of_elements) > maximum_weight:
        return False
    left_index = 0
    right_index = len(list_of_elements) - 1
    while left_index < right_index:
        if list_of_elements[left_index] != list_of_elements[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True