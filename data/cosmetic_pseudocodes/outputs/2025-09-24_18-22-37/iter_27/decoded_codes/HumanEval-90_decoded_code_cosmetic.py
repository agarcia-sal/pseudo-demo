from typing import List, Optional

def next_smallest(vector_of_numbers: List[int]) -> Optional[int]:
    distinct_elements: List[int] = []
    for idx in range(len(vector_of_numbers)):
        curr_val: int = vector_of_numbers[idx]
        if curr_val not in distinct_elements:
            distinct_elements.append(curr_val)
    sorted_elements: List[int] = distinct_elements[:]
    sorted_elements.sort()
    count_vals: int = len(sorted_elements)
    if count_vals >= 2:
        second_element: int = sorted_elements[1]
        return second_element
    else:
        return None