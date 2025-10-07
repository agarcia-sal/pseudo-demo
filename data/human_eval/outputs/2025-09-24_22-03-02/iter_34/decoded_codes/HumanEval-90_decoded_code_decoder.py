from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_set = []
    for element in lst:
        found = False
        for unique_element in unique_set:
            if element == unique_element:
                found = True
                break
        if not found:
            unique_set.append(element)

    sorted_list = []
    while unique_set:
        min_value = unique_set[0]
        min_index = 0
        for i in range(1, len(unique_set)):
            if unique_set[i] < min_value:
                min_value = unique_set[i]
                min_index = i
        sorted_list.append(min_value)
        unique_set.pop(min_index)

    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]