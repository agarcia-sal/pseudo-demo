from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    result_list: List[float] = []
    running_maximum: Optional[float] = None

    for index in range(len(list_of_numbers)):
        if running_maximum is None:
            running_maximum = list_of_numbers[index]
        else:
            if list_of_numbers[index] > running_maximum:
                running_maximum = list_of_numbers[index]
        result_list.append(running_maximum)

    return result_list