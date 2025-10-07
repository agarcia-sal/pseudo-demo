from typing import List

def incr_list(list_l: List[int]) -> List[int]:
    result_list = []
    for element in list_l:
        result_list.append(element + 1)
    return result_list