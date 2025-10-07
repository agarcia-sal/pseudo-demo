from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_list: List[int] = []
    for index in range(len(list_of_elements)):
        current_value: int = list_of_elements[index]
        incremented_value: int = current_value + 1
        result_list.append(incremented_value)
    return result_list