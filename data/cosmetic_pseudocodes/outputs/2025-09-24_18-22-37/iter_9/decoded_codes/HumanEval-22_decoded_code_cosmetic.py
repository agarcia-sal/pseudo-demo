from typing import List, Union

def filter_integers(inputs_array: List[Union[int, object]]) -> List[int]:
    filtered_items: List[int] = []
    for idx in range(len(inputs_array)):
        item = inputs_array[idx]
        if not (not isinstance(item, int)):
            filtered_items.append(item)
    return filtered_items