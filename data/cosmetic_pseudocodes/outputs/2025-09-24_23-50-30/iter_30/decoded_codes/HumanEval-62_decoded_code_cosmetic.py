from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    result_sequence: List[float] = []
    idx: int = 1
    while idx < len(sequence_of_values):
        result_sequence.append(sequence_of_values[idx] * idx)
        idx += 1
    return result_sequence