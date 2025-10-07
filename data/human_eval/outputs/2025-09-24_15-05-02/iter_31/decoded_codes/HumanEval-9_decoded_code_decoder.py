from typing import List, Optional

def rolling_max(list_of_numbers: List[Optional[float]]) -> List[Optional[float]]:
    running_maximum: Optional[float] = None
    result_list: List[Optional[float]] = []

    for number in list_of_numbers:
        if number is None:
            # If current number is None, running_maximum remains unchanged
            result_list.append(running_maximum)
            continue
        if running_maximum is None:
            running_maximum = number
        else:
            running_maximum = max(running_maximum, number)
        result_list.append(running_maximum)

    return result_list