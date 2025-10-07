from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    result: List[float] = []
    for number in list_of_numbers:
        if not (number <= 0):
            result.append(number)
    return result