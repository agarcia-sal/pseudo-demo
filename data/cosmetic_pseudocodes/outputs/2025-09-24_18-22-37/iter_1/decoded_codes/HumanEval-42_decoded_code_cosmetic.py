from typing import List

def incr_list(input_list: List[int]) -> List[int]:
    result_list: List[int] = []
    for item in input_list:
        result_list.append(item + 1)
    return result_list