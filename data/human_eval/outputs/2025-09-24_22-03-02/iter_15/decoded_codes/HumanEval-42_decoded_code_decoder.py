from typing import List

def incr_list(l: List[int]) -> List[int]:
    result = []
    for e in l:
        result.append(e + 1)
    return result