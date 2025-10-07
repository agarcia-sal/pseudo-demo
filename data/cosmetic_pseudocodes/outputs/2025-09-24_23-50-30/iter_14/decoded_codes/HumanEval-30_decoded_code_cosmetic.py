from typing import List

def get_positive(array_of_values: List[float]) -> List[float]:
    results: List[float] = []
    for item in array_of_values:
        if item > 0:
            results.append(item)
    return results