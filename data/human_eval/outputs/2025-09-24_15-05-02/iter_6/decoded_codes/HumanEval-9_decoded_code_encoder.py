from typing import List, Optional

def rolling_max(list_of_numbers: List[Optional[float]]) -> List[Optional[float]]:
    running_max = None
    result = []

    for number in list_of_numbers:
        if running_max is None:
            running_max = number
        else:
            if number is not None:
                if running_max is None or number > running_max:
                    running_max = number
        result.append(running_max)

    return result