from typing import List

def sort_array(array: List[int]) -> List[int]:
    length = len(array)
    if length == 0:
        return []
    else:
        first_element = array[0]
        last_element = array[length - 1]
        sum_first_last = first_element + last_element
        is_sum_even = (sum_first_last % 2) == 0
        copy_array = []
        for index in range(length):
            copy_array.append(array[index])
        copy_array.sort(reverse=is_sum_even)
        return copy_array