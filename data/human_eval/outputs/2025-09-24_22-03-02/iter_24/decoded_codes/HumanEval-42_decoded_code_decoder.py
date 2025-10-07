from typing import List

def incr_list(l: List[int]) -> List[int]:
    result = []
    index = 0
    while index < len(l):
        e = l[index]
        incremented_value = e + 1
        result.append(incremented_value)
        index += 1
    return result