from typing import List

def unique(list_of_elements: List) -> List:
    unique_set = set()
    for element in list_of_elements:
        unique_set.add(element)
    unique_list = list(unique_set)
    sorted_unique_list = sorted(unique_list)
    return sorted_unique_list