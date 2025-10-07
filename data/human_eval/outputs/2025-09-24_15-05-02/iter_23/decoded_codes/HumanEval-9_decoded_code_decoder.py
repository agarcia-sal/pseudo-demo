from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    running_max: Optional[float] = None
    result: List[float] = []

    for number in list_of_numbers:
        if running_max is None:
            running_max = number
        else:
            if number > running_max:
                running_max = number
        result.append(running_max)
    return result