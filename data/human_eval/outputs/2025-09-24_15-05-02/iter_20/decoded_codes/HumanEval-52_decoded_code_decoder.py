from typing import List

def below_threshold(list_l: List[float], threshold_t: float) -> bool:
    for e in list_l:
        if e >= threshold_t:
            return False
    return True