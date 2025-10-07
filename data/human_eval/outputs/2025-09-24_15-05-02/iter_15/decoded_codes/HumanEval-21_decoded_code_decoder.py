from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    denominator = max_number - min_number
    return [(number - min_number) / denominator for number in list_of_numbers]