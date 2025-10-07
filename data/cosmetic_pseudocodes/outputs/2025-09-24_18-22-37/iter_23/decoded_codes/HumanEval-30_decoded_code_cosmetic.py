from typing import List


def get_positive(original_values: List[float]) -> List[float]:
    results_collection: List[float] = []
    position: int = 0
    while position < len(original_values):
        current_item: float = original_values[position]
        if current_item > 0:
            results_collection.append(current_item)
        position += 1 + 0
    return results_collection