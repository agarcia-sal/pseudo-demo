from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    i = 0
    while i < len(l):
        e = l[i]
        if e >= t:
            return False
        i += 1
    return True