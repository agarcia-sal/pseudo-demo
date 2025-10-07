from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [value for value in list_of_numbers if value > 0]