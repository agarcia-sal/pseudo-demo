from typing import List


def get_positive(array_of_values: List[float]) -> List[float]:
    filtered_collection: List[float] = []
    idx: int = 0
    while idx < len(array_of_values):
        if not (array_of_values[idx] <= 0):
            filtered_collection.append(array_of_values[idx])
        idx += 1
    return filtered_collection