from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    if list_of_elements is None:
        raise ValueError("Input list_of_elements cannot be None")
    return [element + 1 for element in list_of_elements]