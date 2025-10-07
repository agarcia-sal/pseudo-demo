from typing import List

def incr_list(items: List[int]) -> List[int]:
    ret: List[int] = []
    idx: int = 0
    while idx < len(items):
        ret.append(items[idx] + 1)
        idx += 1
    return ret