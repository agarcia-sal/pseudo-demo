from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    smallest_value: float = float('inf')
    largest_value: float = float('-inf')
    output_sequence: List[float] = []

    cursor: int = 0
    while cursor < len(sequence_of_values):
        iterator_value: float = sequence_of_values[cursor]
        if iterator_value < smallest_value:
            smallest_value = iterator_value
        if iterator_value > largest_value:
            largest_value = iterator_value
        cursor += 1

    index: int = 0
    denominator: float = largest_value - smallest_value
    while index < len(sequence_of_values):
        iterator_value = sequence_of_values[index]
        numerator: float = iterator_value - smallest_value
        scaled_element: float = numerator / denominator if denominator != 0 else 0.0
        output_sequence.append(scaled_element)
        index += 1

    return output_sequence