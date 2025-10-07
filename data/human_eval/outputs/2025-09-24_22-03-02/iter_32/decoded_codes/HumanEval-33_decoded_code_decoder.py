from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    indexed_elements = []
    indices_with_step = []
    index = 0
    while index < len(l):
        if index % 3 == 0:
            indexed_elements.append(l[index])
            indices_with_step.append(index)
        index += 1
    sorted_elements = sorted(indexed_elements)
    sort_index = 0
    while sort_index < len(sorted_elements):
        index_to_replace = indices_with_step[sort_index]
        l[index_to_replace] = sorted_elements[sort_index]
        sort_index += 1
    return l