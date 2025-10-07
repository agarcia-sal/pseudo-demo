from typing import List


def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []

    first_element = array[0]
    last_element = array[-1]
    sum_ends = first_element + last_element

    descending_flag = (sum_ends % 2) == 0

    sorted_arr = sorted(array)
    if descending_flag:
        sorted_arr.reverse()

    return sorted_arr