from typing import List, Any

def unique(l: List[Any]) -> List[Any]:
    unique_set = {}
    for index in range(len(l)):
        element = l[index]
        unique_set[element] = True
    unique_list = []
    for key in unique_set.keys():
        unique_list.append(key)
    unique_list.sort()
    return unique_list