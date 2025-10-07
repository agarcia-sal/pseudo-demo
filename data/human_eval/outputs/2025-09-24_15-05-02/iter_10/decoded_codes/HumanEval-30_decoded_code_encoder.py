from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    result = []
    for element in list_of_numbers:
        if element > 0:
            result.append(element)
    return result