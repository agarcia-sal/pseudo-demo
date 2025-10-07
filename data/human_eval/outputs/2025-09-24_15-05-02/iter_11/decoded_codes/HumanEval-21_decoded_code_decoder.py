from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_number = min(list_of_numbers)
    max_number = max(list_of_numbers)
    range_size = max_number - min_number
    return [ (element - min_number) / range_size for element in list_of_numbers ]