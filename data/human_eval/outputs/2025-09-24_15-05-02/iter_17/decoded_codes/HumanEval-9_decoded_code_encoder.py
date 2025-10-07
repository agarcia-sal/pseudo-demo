from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    running_max: Optional[float] = None
    result: List[float] = []
    for n in list_of_numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result