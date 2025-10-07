from typing import List

def incr_list(l: List[int]) -> List[int]:
    result: List[int] = []
    for e in l:
        incremented_element = e + 1
        result.append(incremented_element)
    return result