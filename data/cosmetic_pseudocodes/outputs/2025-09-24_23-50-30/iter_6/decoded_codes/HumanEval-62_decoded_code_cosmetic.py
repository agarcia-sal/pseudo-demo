from typing import Sequence, List

def derivative(sequence_of_values: Sequence[int]) -> List[int]:
    result_sequence: List[int] = []
    position: int = 1
    while position < len(sequence_of_values):
        element: int = sequence_of_values[position]
        product: int = position * element
        result_sequence.append(product)
        position += 1
    return result_sequence