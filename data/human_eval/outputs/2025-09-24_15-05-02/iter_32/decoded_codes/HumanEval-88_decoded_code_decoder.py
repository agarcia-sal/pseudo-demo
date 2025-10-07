from typing import List

def sort_array(array_of_non_negative_integers: List[int]) -> List[int]:
    if len(array_of_non_negative_integers) == 0:
        return []
    sum_of_first_and_last: int = array_of_non_negative_integers[0] + array_of_non_negative_integers[-1]
    should_sort_in_descending: bool = (sum_of_first_and_last % 2 == 0)
    return sorted(array_of_non_negative_integers, reverse=should_sort_in_descending)