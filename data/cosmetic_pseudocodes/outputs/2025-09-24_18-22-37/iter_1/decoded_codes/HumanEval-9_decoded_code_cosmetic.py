from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    result_list: List[int] = []
    running_maximum: Optional[int] = None

    for index in range(len(list_of_numbers)):
        if running_maximum is None:
            running_maximum = list_of_numbers[index]
        else:
            if list_of_numbers[index] > running_maximum:
                running_maximum = list_of_numbers[index]
        result_list.append(running_maximum)

    return result_list