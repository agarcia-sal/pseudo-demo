from typing import List, Any

def below_threshold(list_l: List[Any], threshold_t: Any) -> bool:
    for e in list_l:
        if e >= threshold_t:
            return False
    return True