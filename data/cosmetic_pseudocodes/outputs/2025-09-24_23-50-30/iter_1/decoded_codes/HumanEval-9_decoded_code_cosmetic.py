from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    result_list: List[float] = []
    running_maximum: Optional[float] = None

    index: int = 0
    while index < len(list_of_numbers):
        number = list_of_numbers[index]
        if running_maximum is None:
            running_maximum = number
        elif number > running_maximum:
            running_maximum = number
        result_list.append(running_maximum)
        index += 1

    return result_list