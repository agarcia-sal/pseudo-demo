from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    subset_indices = []
    subset_values = []
    result = list(l)
    length_l = len(l)
    index = 0
    while index < length_l:
        if index % 3 == 0:
            subset_indices.append(index)
            subset_values.append(l[index])
        index += 1
    sorted_values = sorted(subset_values)
    i = 0
    while i < len(subset_indices):
        index_to_set = subset_indices[i]
        value_to_set = sorted_values[i]
        result[index_to_set] = value_to_set
        i += 1
    return result