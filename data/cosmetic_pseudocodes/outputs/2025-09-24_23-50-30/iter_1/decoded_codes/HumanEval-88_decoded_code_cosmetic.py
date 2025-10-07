from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    first_element = array[0]
    last_element = array[-1]
    total = first_element + last_element
    sort_desc = (total % 2 == 0)
    return sorted(array, reverse=sort_desc)