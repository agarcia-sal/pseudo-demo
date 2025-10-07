from typing import List

def unique(l: List) -> List:
    unique_elements = set()
    for i in range(len(l)):
        unique_elements.add(l[i])
    unique_list = list(unique_elements)
    sorted_unique_list = sorted(unique_list)
    return sorted_unique_list