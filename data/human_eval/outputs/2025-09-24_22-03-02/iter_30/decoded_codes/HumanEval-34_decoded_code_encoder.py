from typing import List

def unique(l: List) -> List:
    temp_set = set()
    for each_index in range(len(l)):
        temp_element = l[each_index]
        temp_set.add(temp_element)
    temp_list = []
    for each_element in temp_set:
        temp_list.append(each_element)
    temp_list.sort()
    return temp_list