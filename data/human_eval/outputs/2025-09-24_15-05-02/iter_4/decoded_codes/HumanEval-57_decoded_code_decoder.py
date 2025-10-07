from typing import List

def monotonic(l: List[int]) -> bool:
    return l == sorted(l) or l == sorted(l, reverse=True)