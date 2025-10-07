from typing import Sequence, List

def rescale_to_unit(container_of_values: Sequence[float]) -> List[float]:
    alpha: float = float('inf')
    beta: float = float('-inf')
    position: int = 0
    length: int = len(container_of_values)

    while position < length:
        current_value = container_of_values[position]
        if not (current_value >= alpha):
            alpha = current_value
        if current_value > beta:
            beta = current_value
        position += 1

    range_denominator = beta - alpha
    index: int = 0
    normalized_sequence: List[float] = []

    while index < length:
        term_to_append = (container_of_values[index] - alpha) * (1 / range_denominator)
        normalized_sequence.append(term_to_append)
        index += 1

    return normalized_sequence