from typing import List

def unique(l: List) -> List:
    unique_set = set()
    for index in range(len(l)):
        unique_set.add(l[index])
    unique_list = []
    for element in unique_set:
        unique_list.append(element)
    sorted_list = sorted(unique_list)
    return sorted_list