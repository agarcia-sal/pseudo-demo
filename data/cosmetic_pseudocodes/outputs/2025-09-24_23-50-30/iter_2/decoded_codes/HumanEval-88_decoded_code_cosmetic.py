from typing import List

def sort_array(arr: List[int]) -> List[int]:
    if not arr:
        return []
    first_element = arr[0]
    last_element = arr[-1]
    parity_check = (first_element + last_element) % 2
    descending_mode = parity_check == 0
    sorted_arr = sorted(arr)
    if descending_mode:
        return sorted_arr[::-1]
    return sorted_arr