from typing import List

def monotonic(l: List) -> bool:
    sorted_list = sorted(l)
    sorted_list_reverse = sorted(l, reverse=True)
    return l == sorted_list or l == sorted_list_reverse