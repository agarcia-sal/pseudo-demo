from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    minimum_number: float = min(list_of_numbers)
    maximum_number: float = max(list_of_numbers)
    denominator: float = maximum_number - minimum_number
    if denominator == 0:
        # Avoid division by zero: return zeros if all numbers are the same
        return [0.0 for _ in list_of_numbers]
    return [(each_number - minimum_number) / denominator for each_number in list_of_numbers]