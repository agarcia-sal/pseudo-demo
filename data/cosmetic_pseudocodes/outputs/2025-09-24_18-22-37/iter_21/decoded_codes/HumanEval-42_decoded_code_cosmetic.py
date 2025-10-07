from typing import Sequence, List

def incr_list(sequence_of_values: Sequence[int]) -> List[int]:
    incremented_sequence: List[int] = []
    current_index: int = 0
    while current_index < len(sequence_of_values):
        current_element: int = sequence_of_values[current_index]
        updated_element: int = current_element + 1
        incremented_sequence.append(updated_element)
        current_index += 1
    return incremented_sequence