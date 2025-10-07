from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    filtered_collection: List[float] = []
    idx: int = 0
    while idx < len(list_of_numbers):
        item: float = list_of_numbers[idx]
        if not (item <= 0):
            filtered_collection.append(item)
        idx += 1
    return filtered_collection