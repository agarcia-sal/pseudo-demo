from typing import List

def monotonic(l: List) -> bool:
    return l == sorted(l) or l == sorted(l, reverse=True)