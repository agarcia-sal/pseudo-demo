from typing import Sequence, List

def get_positive(sequence_of_values: Sequence[int]) -> List[int]:
    filtered_elements: List[int] = []
    position: int = 0
    while position < len(sequence_of_values):
        current_item: int = sequence_of_values[position]
        if current_item > 0:
            filtered_elements.append(current_item)
        position += 1
    return filtered_elements