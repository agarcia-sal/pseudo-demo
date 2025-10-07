from typing import List

def get_positive(array_elements: List[float]) -> List[float]:
    result_collection: List[float] = []
    idx: int = 0

    while idx < len(array_elements):
        if not (array_elements[idx] <= 0):
            result_collection.append(array_elements[idx])
        idx += 1

    return result_collection