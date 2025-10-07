from typing import List, Optional, Union

def pluck(collection: List[int]) -> List[Union[int, int]]:
    found_values: dict[int, bool] = {}
    i: int = 0

    while i < len(collection):
        if (collection[i] // 2) * 2 == collection[i]:
            found_values[collection[i]] = True
        i += 1

    if not found_values:
        return []

    min_value: Optional[int] = None
    for key in found_values.keys():
        if min_value is None or key < min_value:
            min_value = key

    index_of_min: int = 0
    while index_of_min < len(collection):
        if collection[index_of_min] == min_value:
            break
        index_of_min += 1

    return [min_value, index_of_min]