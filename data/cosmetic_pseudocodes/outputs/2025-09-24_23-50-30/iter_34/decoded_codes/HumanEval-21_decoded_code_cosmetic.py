from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    a = min(sequence_of_values)
    b = max(sequence_of_values)
    if a == b:
        # Avoid division by zero if all elements are equal; return zeros
        return [0.0] * len(sequence_of_values)
    return [(x - a) / (b - a) for x in sequence_of_values]