from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    new_list: List[int] = []
    iterator: int = 0
    while iterator < len(list_of_elements):
        item: int = list_of_elements[iterator]
        modified_value: int = item + 1
        new_list.append(modified_value)
        iterator += 1
    return new_list