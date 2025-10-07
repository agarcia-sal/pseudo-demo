from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    running_maximum: Optional[float] = None
    rolling_maximums: List[float] = []
    for number in list_of_numbers:
        if running_maximum is None:
            running_maximum = number
        else:
            running_maximum = max(running_maximum, number)
        rolling_maximums.append(running_maximum)
    return rolling_maximums