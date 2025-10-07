from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    return [sequence_of_values[index] * index for index in range(1, len(sequence_of_values))]