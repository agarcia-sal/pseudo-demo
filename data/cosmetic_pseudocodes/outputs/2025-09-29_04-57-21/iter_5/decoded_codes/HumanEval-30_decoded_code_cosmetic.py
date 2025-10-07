from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [item for item in list_of_numbers if item > 0]