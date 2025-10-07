from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    return [e for e in list_of_numbers if e > 0]