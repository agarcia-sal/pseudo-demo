from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []
    first_element = input_list[0]
    last_element = input_list[-1]
    sum_edges = first_element + last_element
    descending_flag = (sum_edges % 2 == 0)
    return sorted(input_list, reverse=descending_flag)