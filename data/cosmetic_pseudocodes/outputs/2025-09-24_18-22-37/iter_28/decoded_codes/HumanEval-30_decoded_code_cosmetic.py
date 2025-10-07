from typing import List

def get_positive(array_of_values: List[float]) -> List[float]:
    collected: List[float] = []
    current_index: int = 0
    while current_index < len(array_of_values):
        candidate = array_of_values[current_index]
        if candidate > 0:
            collected.append(candidate)
        current_index += 1
    return collected