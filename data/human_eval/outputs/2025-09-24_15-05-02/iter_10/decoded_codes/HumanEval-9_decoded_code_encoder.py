from typing import List, Optional

def rolling_max(list_of_numbers: List[Optional[float]]) -> List[Optional[float]]:
    running_max: Optional[float] = None
    result: List[Optional[float]] = []

    for number in list_of_numbers:
        if running_max is None:
            running_max = number
        else:
            if running_max > number:
                pass  # keep running_max
            else:
                running_max = number
        result.append(running_max)

    return result