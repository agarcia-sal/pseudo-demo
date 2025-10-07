from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    lower_bound: float = float('inf')
    upper_bound: float = float('-inf')
    for element in array_of_values:
        if element < lower_bound:
            lower_bound = element
        if element > upper_bound:
            upper_bound = element
    scale_factor: float = upper_bound - lower_bound
    if scale_factor == 0:
        # All elements are equal; map them to 0.0 to avoid division by zero.
        return [0.0 for _ in array_of_values]
    normalized_array: List[float] = [(value - lower_bound) / scale_factor for value in array_of_values]
    return normalized_array