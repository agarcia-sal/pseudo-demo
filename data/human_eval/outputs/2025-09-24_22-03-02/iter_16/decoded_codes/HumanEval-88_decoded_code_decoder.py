from copy import copy
from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    else:
        sum_first_last = array[0] + array[-1]
        is_even = (sum_first_last % 2) == 0
        array_copy = copy(array)
        if is_even:
            array_copy.sort(reverse=True)
        else:
            array_copy.sort()
        return array_copy