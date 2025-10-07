from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    return [i * sequence_of_values[i] for i in range(1, len(sequence_of_values))]