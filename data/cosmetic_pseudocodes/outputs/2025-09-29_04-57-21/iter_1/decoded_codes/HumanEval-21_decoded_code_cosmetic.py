from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val: float = min(list_of_numbers)
    max_val: float = max(list_of_numbers)
    scale_factor: float = max_val - min_val
    if scale_factor == 0:
        # All elements are equal; return zeros
        return [0.0 for _ in list_of_numbers]
    return [(element - min_val) / scale_factor for element in list_of_numbers]