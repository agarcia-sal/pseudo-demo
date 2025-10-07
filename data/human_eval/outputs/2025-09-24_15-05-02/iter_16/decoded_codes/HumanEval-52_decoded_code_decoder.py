from typing import List

def below_threshold(list_l: List[float], threshold_t: float) -> bool:
    for element_e in list_l:
        if element_e >= threshold_t:
            return False
    return True