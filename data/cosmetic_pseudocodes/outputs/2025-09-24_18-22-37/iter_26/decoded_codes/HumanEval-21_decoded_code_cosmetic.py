from typing import Sequence, List

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    smallest_element: float = float('inf')
    largest_element: float = float('-inf')

    for val in input_sequence:
        if val < smallest_element:
            smallest_element = val
        if val > largest_element:
            largest_element = val

    denominator = largest_element - smallest_element
    if denominator == 0:
        # Avoid division by zero: all elements are equal, map all to 0.0
        return [0.0 for _ in input_sequence]

    return [(val - smallest_element) / denominator for val in input_sequence]