from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    new_list: List[int] = []
    for index in range(len(list_of_elements)):
        new_list.append(list_of_elements[index] + 1)
    return new_list