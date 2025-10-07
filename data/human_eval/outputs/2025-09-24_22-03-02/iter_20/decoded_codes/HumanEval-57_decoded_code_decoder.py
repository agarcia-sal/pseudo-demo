from typing import List

def monotonic(l: List[int]) -> bool:
    if l == sorted(l):
        return True
    elif l == sorted(l, reverse=True):
        return True
    else:
        return False