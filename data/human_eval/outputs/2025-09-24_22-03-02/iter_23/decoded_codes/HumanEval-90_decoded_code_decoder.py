from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    unique_list = []
    temp_set = []
    for index in range(len(lst)):
        current_element = lst[index]
        found = False
        for set_index in range(len(temp_set)):
            if temp_set[set_index] == current_element:
                found = True
                break
        if not found:
            temp_set.append(current_element)
    for i in range(len(temp_set) - 1):
        for j in range(len(temp_set) - 1 - i):
            if temp_set[j] > temp_set[j + 1]:
                temp_value = temp_set[j]
                temp_set[j] = temp_set[j + 1]
                temp_set[j + 1] = temp_value
    unique_list = temp_set
    if len(unique_list) < 2:
        return None
    else:
        return unique_list[1]