from typing import Sequence, List

def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    minimum_value: float = float('inf')
    maximum_value: float = float('-inf')
    for element in sequence:
        if element < minimum_value:
            minimum_value = element
        if element > maximum_value:
            maximum_value = element
    diff: float = maximum_value - minimum_value
    if diff == 0:
        # All elements are the same; return zeros to avoid division by zero.
        return [0.0 for _ in sequence]
    index: int = 0
    output_list: List[float] = []
    while index < len(sequence):
        output_list.append((sequence[index] - minimum_value) / diff)
        index += 1
    return output_list