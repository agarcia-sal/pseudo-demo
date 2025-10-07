from typing import List

def rescale_to_unit(values: List[float]) -> List[float]:
    low_bound: float = float('inf')
    high_bound: float = float('-inf')
    for idx in range(len(values)):
        if values[idx] < low_bound:
            low_bound = values[idx]
        if values[idx] > high_bound:
            high_bound = values[idx]

    range_ = high_bound - low_bound
    if range_ == 0:
        # Avoid division by zero; all values are identical, map them to 0.0
        return [0.0 for _ in values]

    result_collection: List[float] = []
    index: int = 0
    while index < len(values):
        result_collection.append((values[index] - low_bound) / range_)
        index += 1

    return result_collection