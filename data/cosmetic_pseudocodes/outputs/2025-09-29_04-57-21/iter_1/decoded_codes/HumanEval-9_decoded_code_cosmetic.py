from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    running_maximum: Optional[int] = None
    result_list: List[int] = []

    index: int = 0
    while index < len(list_of_numbers):
        current_element = list_of_numbers[index]

        if running_maximum is None:
            running_maximum = current_element
        elif current_element > running_maximum:
            running_maximum = current_element

        result_list.append(running_maximum)
        index += 1

    return result_list