from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    indices_to_sort = []
    values_to_sort = []
    length_to_sort = len(l)
    index = 0
    while index < length_to_sort:
        if index % 3 == 0:
            indices_to_sort.append(index)
            values_to_sort.append(l[index])
        index += 1
    sorted_values = sorted(values_to_sort)
    index_sorted = 0
    while index_sorted < len(indices_to_sort):
        l[indices_to_sort[index_sorted]] = sorted_values[index_sorted]
        index_sorted += 1
    return l