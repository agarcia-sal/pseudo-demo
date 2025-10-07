from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    dict_values_indices = {
        value: idx
        for idx, value in enumerate(array_of_nodes)
        if value % 2 == 0
    }

    if not dict_values_indices:
        return []

    list_of_keys = list(dict_values_indices.keys())

    min_key = list_of_keys[0]
    for v in list_of_keys[1:]:
        if v < min_key:
            min_key = v

    return [min_key, dict_values_indices[min_key]]