from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [num for num in list_of_numbers if num > 0]