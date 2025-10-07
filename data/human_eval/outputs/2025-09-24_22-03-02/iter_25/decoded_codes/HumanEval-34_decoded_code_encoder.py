from typing import List

def unique(l: List) -> List:
    unique_set = []
    for i in range(len(l)):
        element = l[i]
        found = False
        for j in range(len(unique_set)):
            if unique_set[j] == element:
                found = True
                break
        if not found:
            unique_set.append(element)
    sorted_list = []
    while len(unique_set) > 0:
        min_element = unique_set[0]
        min_index = 0
        for k in range(1, len(unique_set)):
            if unique_set[k] < min_element:
                min_element = unique_set[k]
                min_index = k
        sorted_list.append(min_element)
        unique_set.pop(min_index)
    return sorted_list