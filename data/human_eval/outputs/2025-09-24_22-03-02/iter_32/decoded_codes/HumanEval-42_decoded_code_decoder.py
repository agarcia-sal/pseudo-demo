from typing import List

def incr_list(l: List[int]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(l):
        element = l[index]
        incremented_element = element + 1
        result.append(incremented_element)
        index += 1
    return result