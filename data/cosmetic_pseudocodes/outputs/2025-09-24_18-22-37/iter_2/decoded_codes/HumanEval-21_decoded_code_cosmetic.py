from typing import Iterable, List

def rescale_to_unit(numbers_collection: Iterable[float]) -> List[float]:
    min_val = float('inf')
    max_val = float('-inf')
    for element in numbers_collection:
        if element < min_val:
            min_val = element
        if element > max_val:
            max_val = element
    range_val = max_val - min_val
    if range_val == 0:
        # avoid division by zero: all values are identical, scale them all to 0
        return [0.0 for _ in numbers_collection]
    return [(value - min_val) / range_val for value in numbers_collection]