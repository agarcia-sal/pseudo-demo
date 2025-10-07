from typing import List, Optional

def longest(arr: List[str]) -> Optional[str]:
    if not arr:
        return None

    n: int = -1
    i: int = 0
    while i < len(arr):
        x: int = len(arr[i])
        if x > n:
            n = x
        i += 1

    i = 0
    while i < len(arr):
        if len(arr[i]) == n:
            return arr[i]
        i += 1

    return None