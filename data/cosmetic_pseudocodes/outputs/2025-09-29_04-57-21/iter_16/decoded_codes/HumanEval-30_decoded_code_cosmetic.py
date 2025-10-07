from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [number for number in list_of_numbers if number > 0]