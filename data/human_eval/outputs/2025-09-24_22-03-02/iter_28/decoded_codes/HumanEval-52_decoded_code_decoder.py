from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    index = 0
    while index < len(l):
        e = l[index]
        if e >= t:
            return False
        index += 1
    return True