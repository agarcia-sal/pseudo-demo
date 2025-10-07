from typing import List

def incr_list(l: List[int]) -> List[int]:
    result_list = []
    for index in range(len(l)):
        e = l[index]
        incremented_value = e + 1
        result_list.append(incremented_value)
    return result_list