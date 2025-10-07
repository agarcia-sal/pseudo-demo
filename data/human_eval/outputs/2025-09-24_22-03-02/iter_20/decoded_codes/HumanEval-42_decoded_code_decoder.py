from typing import List

def incr_list(l: List[int]) -> List[int]:
    result: List[int] = []
    for index in range(len(l)):
        e = l[index]
        incremented_element = e + 1
        result.append(incremented_element)
    return result