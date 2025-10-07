from typing import List

def below_threshold(l: List[float], t: float) -> bool:
    for element in l:
        if element >= t:
            return False
    return True