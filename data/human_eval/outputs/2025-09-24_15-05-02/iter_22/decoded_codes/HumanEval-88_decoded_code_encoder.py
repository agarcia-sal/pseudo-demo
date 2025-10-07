from typing import List

def sort_array(input_array: List[int]) -> List[int]:
    if len(input_array) == 0:
        return []
    sum_of_first_and_last: int = input_array[0] + input_array[-1]
    sort_in_descending_order: bool = (sum_of_first_and_last % 2 == 0)
    sorted_array: List[int] = sorted(input_array, reverse=sort_in_descending_order)
    return sorted_array