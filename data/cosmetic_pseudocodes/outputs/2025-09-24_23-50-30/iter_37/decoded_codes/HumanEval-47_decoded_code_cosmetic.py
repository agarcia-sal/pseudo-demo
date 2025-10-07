from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_collection: List[Union[int, float]] = []
    for item in list_of_elements:
        sorted_collection.append(item)
    sorted_collection.sort()
    count: int = len(sorted_collection)

    if count % 2 == 0:
        lower_idx: int = (count // 2) - 1
        upper_idx: int = count // 2
        result: float = (sorted_collection[lower_idx] + sorted_collection[upper_idx]) / 2.0
    else:
        mid_idx: int = count // 2
        result: float = float(sorted_collection[mid_idx])

    return result