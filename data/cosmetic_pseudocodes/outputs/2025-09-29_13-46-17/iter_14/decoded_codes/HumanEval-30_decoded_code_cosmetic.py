from typing import List, Set

def get_positive(list_of_numbers: List[float]) -> Set[float]:
    result: Set[float] = set()
    index: int = 0
    while index < len(list_of_numbers):
        value = list_of_numbers[index]
        if value > 0:
            result.add(value)
        index += 1
    return result