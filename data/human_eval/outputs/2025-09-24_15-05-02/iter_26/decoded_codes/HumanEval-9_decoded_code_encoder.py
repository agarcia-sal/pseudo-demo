from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    running_max: Optional[int] = None
    result: List[int] = []

    for number in list_of_numbers:
        if running_max is None:
            running_max = number
        else:
            running_max = max(running_max, number)

        result.append(running_max)

    return result