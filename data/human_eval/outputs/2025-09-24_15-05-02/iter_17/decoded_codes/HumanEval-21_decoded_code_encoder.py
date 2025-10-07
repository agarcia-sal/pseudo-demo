from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number: float = min(list_of_numbers)
    max_number: float = max(list_of_numbers)
    denominator: float = max_number - min_number
    result: List[float] = []
    if denominator == 0:
        # Avoid division by zero; if all numbers are the same, map all to 0.0
        result = [0.0 for _ in list_of_numbers]
    else:
        for x in list_of_numbers:
            result.append((x - min_number) / denominator)
    return result