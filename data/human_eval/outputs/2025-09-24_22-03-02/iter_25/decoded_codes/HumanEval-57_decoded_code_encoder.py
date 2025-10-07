from typing import List

def monotonic(l: List) -> bool:
    sorted_l = sorted(l)
    sorted_l_reverse = sorted(l, reverse=True)
    if l == sorted_l or l == sorted_l_reverse:
        return True
    else:
        return False