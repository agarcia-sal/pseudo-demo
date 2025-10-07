from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    valid_numbers: List[int] = []
    iterator: int = 0
    while iterator < len(list_of_values):
        candidate = list_of_values[iterator]
        if isinstance(candidate, int):
            valid_numbers.append(candidate)
        iterator += 1
    return valid_numbers