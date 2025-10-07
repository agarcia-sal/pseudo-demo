from typing import List, Union

def sort_array(collection: List[Union[int, float]]) -> List[Union[int, float]]:
    if not collection:
        return []
    first_element = collection[0]
    last_index = len(collection) - 1
    last_element = collection[last_index]
    sum_extremes = first_element + last_element
    descending_flag: bool = (sum_extremes % 2 == 0)
    return sorted(collection, reverse=descending_flag)