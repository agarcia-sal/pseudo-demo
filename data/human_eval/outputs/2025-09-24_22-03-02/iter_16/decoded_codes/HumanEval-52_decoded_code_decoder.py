from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    for e in l:
        if e >= t:
            return False
    return True