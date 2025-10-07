from typing import List

def incr_list(h: List[int]) -> List[int]:
    def i(a: List[int], x: int) -> List[int]:
        if x == len(a):
            return []
        else:
            return [a[x] + 1] + i(a, x + 1)
    return i(h, 0)