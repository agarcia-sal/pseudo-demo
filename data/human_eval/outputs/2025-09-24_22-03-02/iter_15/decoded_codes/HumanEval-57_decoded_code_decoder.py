from typing import List

def monotonic(l: List) -> bool:
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    else:
        return False