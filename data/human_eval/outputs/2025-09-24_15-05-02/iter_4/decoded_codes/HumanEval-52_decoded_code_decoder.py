from typing import List

def below_threshold(l: List[int], t: int) -> bool:
    for element in l:
        if element >= t:
            return False
    return True