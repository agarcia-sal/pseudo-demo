from typing import List

def get_positive(array_of_values: List[float]) -> List[float]:
    result_collection: List[float] = []
    idx_marker: int = 0
    while idx_marker < len(array_of_values):
        current_item = array_of_values[idx_marker]
        if current_item > 0:
            result_collection.append(current_item)
        idx_marker += 1
    return result_collection