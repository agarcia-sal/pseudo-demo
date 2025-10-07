from typing import List

def incr_list(l: List[int]) -> List[int]:
    result: List[int] = []
    i: int = 0
    while i < len(l):
        e: int = l[i]
        incremented_e: int = e + 1
        result.append(incremented_e)
        i += 1
    return result