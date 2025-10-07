from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    denominator = max_number - min_number
    if denominator == 0:
        return [0.0 for _ in list_of_numbers]  # all elements are equal, map to 0.0
    return [(number - min_number) / denominator for number in list_of_numbers]