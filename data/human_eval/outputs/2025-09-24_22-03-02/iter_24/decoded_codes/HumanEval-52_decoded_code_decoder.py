from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    for i in range(len(l)):
        e = l[i]
        if e >= t:
            return False
    return True