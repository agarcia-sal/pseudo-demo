from typing import List

def unique(l: List) -> List:
    temp_set = set()
    for index in range(len(l)):
        temp_set.add(l[index])
    temp_list = []
    for element in temp_set:
        temp_list.append(element)
    temp_list.sort()
    return temp_list