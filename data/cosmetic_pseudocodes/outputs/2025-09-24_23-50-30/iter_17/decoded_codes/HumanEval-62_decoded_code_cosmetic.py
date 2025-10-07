from typing import Sequence, List

def derivative(input_sequence: Sequence[float]) -> List[float]:
    return [input_sequence[position] * position for position in range(1, len(input_sequence))]