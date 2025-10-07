from typing import List

def sort_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    else:
        sum_first_last = array[0] + array[-1]
        is_sum_even = (sum_first_last % 2 == 0)
        copy_array = list(array)
        if is_sum_even:
            return sorted(copy_array, reverse=True)
        else:
            return sorted(copy_array)