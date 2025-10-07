from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_elements: List[int] = []
    temp_set: List[int] = []
    for index in range(len(lst)):
        current_element = lst[index]
        is_in_set = False
        for set_index in range(len(temp_set)):
            if temp_set[set_index] == current_element:
                is_in_set = True
                break
        if not is_in_set:
            temp_set.append(current_element)
    while len(temp_set) > 0:
        min_value = temp_set[0]
        min_index = 0
        for check_index in range(1, len(temp_set)):
            if temp_set[check_index] < min_value:
                min_value = temp_set[check_index]
                min_index = check_index
        unique_elements.append(min_value)
        temp_set.pop(min_index)
    if len(unique_elements) < 2:
        return None
    else:
        return unique_elements[1]