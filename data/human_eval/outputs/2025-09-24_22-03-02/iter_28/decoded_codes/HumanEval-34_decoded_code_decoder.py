from typing import List

def unique(l: List) -> List:
    unique_set = set()
    for index in range(len(l)):
        unique_set.add(l[index])
    unique_list = []
    for element in list(unique_set):
        unique_list.append(element)
    unique_list.sort()
    return unique_list