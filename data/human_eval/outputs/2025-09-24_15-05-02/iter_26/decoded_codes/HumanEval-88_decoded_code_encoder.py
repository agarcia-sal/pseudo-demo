from typing import List

def sort_array(array_of_non_negative_integers: List[int]) -> List[int]:
    if not array_of_non_negative_integers:
        return []
    sum_of_first_and_last: int = array_of_non_negative_integers[0] + array_of_non_negative_integers[-1]
    is_sum_even: bool = (sum_of_first_and_last % 2 == 0)
    return sorted(array_of_non_negative_integers, reverse=is_sum_even)