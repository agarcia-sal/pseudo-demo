from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [element for element in list_of_numbers if element > 0]