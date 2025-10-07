from typing import Sequence, List

def rescale_to_unit(sequence_values: Sequence[float]) -> List[float]:
    if not sequence_values:
        return []

    smallest_value = sequence_values[0]
    largest_value = sequence_values[0]

    for index in range(1, len(sequence_values)):
        value = sequence_values[index]
        if value < smallest_value:
            smallest_value = value
        elif value > largest_value:
            largest_value = value

    span = largest_value - smallest_value
    if span == 0:
        return [0.0 for _ in sequence_values]

    adjusted_values = []
    idx = 0
    while idx < len(sequence_values):
        value = sequence_values[idx]
        adjusted_values.append((value - smallest_value) / span)
        idx += 1

    return adjusted_values