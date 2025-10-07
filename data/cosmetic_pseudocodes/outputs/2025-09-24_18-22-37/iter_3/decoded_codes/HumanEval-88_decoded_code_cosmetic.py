from typing import List

def sort_array(array: List[int]) -> List[int]:
    if not array:
        return []
    total = array[0] + array[-1]
    desc_flag = (total % 2 == 0)
    result = array.copy()
    result.sort(reverse=desc_flag)
    return result