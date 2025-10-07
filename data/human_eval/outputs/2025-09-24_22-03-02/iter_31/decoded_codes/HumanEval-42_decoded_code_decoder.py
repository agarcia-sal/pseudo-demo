from typing import List

def incr_list(l: List[int]) -> List[int]:
    result = []
    index = 0
    length = len(l)
    while index < length:
        e = l[index]
        incremented_element = e + 1
        result.append(incremented_element)
        index += 1
    return result