from typing import Sequence, List

def rescale_to_unit(numbers_collection: Sequence[float]) -> List[float]:
    if not numbers_collection:
        return []

    min_value: float = float('inf')
    max_value: float = float('-inf')

    for idx in range(len(numbers_collection)):
        val = numbers_collection[idx]
        if val > max_value:
            max_value = val
        if val < min_value:
            min_value = val

    size_diff = max_value - min_value
    if size_diff == 0:
        # Avoid division by zero; return zeros if all values are equal
        return [0.0 for _ in numbers_collection]

    scaled_values: List[float] = []
    pos_loop = 0
    while pos_loop < len(numbers_collection):
        scaled_values.append((numbers_collection[pos_loop] - min_value) / size_diff)
        pos_loop += 1

    return scaled_values