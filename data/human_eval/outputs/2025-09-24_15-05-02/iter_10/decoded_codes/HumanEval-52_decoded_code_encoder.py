from typing import List

def below_threshold(list_l: List[int], int_t: int) -> bool:
    for element in list_l:
        if element >= int_t:
            return False
    return True