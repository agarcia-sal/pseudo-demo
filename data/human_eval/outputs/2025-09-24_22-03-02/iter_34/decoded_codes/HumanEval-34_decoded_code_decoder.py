from typing import List

def unique(l: List) -> List:
    temp_set = set()
    index = 0
    while index < len(l):
        temp_set.add(l[index])
        index += 1
    temp_list = []
    for element in temp_set:
        temp_list.append(element)
    i = 0
    while i < len(temp_list) - 1:
        j = i + 1
        while j < len(temp_list):
            if temp_list[i] > temp_list[j]:
                temp = temp_list[i]
                temp_list[i] = temp_list[j]
                temp_list[j] = temp
            j += 1
        i += 1
    sorted_list = temp_list
    return sorted_list