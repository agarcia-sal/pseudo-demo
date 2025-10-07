from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    total_elements: int = len(input_list)
    if total_elements == 0:
        return []
    first_element: int = input_list[0]
    last_element: int = input_list[total_elements - 1]
    sum_ends: int = first_element + last_element

    descending_flag: bool = False
    if (sum_ends % 2) == 0:
        descending_flag = True
    else:
        descending_flag = False

    sorted_list: List[int] = input_list.copy()
    if descending_flag:
        sorted_list.sort(reverse=True)
    else:
        sorted_list.sort()

    return sorted_list