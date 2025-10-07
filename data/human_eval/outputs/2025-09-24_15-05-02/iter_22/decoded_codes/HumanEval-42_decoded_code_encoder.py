from typing import List

def incr_list(list_of_numbers: List[int]) -> List[int]:
    incremented_list: List[int] = []
    for element in list_of_numbers:
        incremented_list.append(element + 1)
    return incremented_list