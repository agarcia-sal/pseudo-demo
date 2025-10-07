from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    third_elements = []
    index = 0
    while index < len(l):
        third_elements.append(l[index])
        index += 3
    sorted_third_elements = sorted(third_elements)
    index = 0
    sorted_index = 0
    while index < len(l):
        l[index] = sorted_third_elements[sorted_index]
        index += 3
        sorted_index += 1
    return l