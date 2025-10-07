from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    positive_numbers: List[float] = []
    for element in list_of_numbers:
        if element > 0:
            positive_numbers.append(element)
    return positive_numbers