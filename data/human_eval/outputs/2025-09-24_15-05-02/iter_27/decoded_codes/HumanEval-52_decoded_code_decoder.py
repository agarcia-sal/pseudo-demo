from typing import List

def below_threshold(list_l: List[float], threshold_t: float) -> bool:
    for element in list_l:
        if element >= threshold_t:
            return False
    return True