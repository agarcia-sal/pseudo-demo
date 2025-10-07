from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    filtered_values: List[float] = []
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_item: float = list_of_numbers[iterator]
        if not (current_item <= 0):
            filtered_values.append(current_item)
        iterator += 1
    return filtered_values