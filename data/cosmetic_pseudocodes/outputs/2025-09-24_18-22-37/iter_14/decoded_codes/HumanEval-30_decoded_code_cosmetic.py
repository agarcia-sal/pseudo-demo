from typing import List

def get_positive(array_elements: List[int]) -> List[int]:
    result_collection: List[int] = []
    idx: int = 0
    while idx < len(array_elements):
        current_value: int = array_elements[idx]
        if current_value > 0:
            result_collection.append(current_value)
        idx += 1
    return result_collection