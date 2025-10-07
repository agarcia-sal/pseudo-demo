from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_set = []
    for index in range(len(lst) - 1):
        current_element = lst[index]
        element_found = False
        for set_index in range(len(unique_set)):
            if unique_set[set_index] == current_element:
                element_found = True
                break
        if not element_found:
            unique_set.append(current_element)
    sorted_lst = []
    while len(unique_set) > 0:
        min_element = unique_set[0]
        min_index = 0
        for i in range(1, len(unique_set)):
            if unique_set[i] < min_element:
                min_element = unique_set[i]
                min_index = i
        sorted_lst.append(min_element)
        unique_set.pop(min_index)
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]