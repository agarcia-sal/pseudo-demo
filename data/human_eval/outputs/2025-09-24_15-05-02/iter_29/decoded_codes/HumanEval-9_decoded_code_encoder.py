from typing import List, Optional

def rolling_max(list_of_integers: List[int]) -> List[int]:
    running_maximum: Optional[int] = None
    result_list: List[int] = []

    for integer in list_of_integers:
        if running_maximum is None:
            running_maximum = integer
        else:
            running_maximum = max(running_maximum, integer)
        result_list.append(running_maximum)

    return result_list