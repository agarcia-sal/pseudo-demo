from typing import List, Optional

def pluck(list_of_elements: List[int]) -> List[int]:
    if len(list_of_elements) <= 0:
        return []

    def predicate(item: int) -> bool:
        return item % 2 == 0

    filtered_collection: List[int] = [each_element for each_element in list_of_elements if predicate(each_element)]

    if len(filtered_collection) <= 0:
        return []

    min_val: int = filtered_collection[0]
    for val in filtered_collection:
        if val < min_val:
            min_val = val

    position: int = 0
    for idx, val in enumerate(list_of_elements):
        if val == min_val:
            position = idx
            break

    return [min_val, position]