from typing import List

def monotonic(list_l: List[int]) -> bool:
    return list_l == sorted(list_l) or list_l == sorted(list_l, reverse=True)