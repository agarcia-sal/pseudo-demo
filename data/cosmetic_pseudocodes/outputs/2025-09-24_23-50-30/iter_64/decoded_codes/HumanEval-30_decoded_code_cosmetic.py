from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    result: List[float] = []
    idx: int = 0
    while idx < len(list_of_numbers):
        if not (list_of_numbers[idx] <= 0):
            result.append(list_of_numbers[idx])
        idx += 1
    return result