from typing import Sequence, List


def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    if not sequence:
        return []
    smallest: float = sequence[0]
    largest: float = sequence[0]

    for idx in range(1, len(sequence)):
        if sequence[idx] < smallest:
            smallest = sequence[idx]
        elif sequence[idx] > largest:
            largest = sequence[idx]

    range_ = largest - smallest
    if range_ == 0:
        # All elements are equal, return zeros.
        return [0.0] * len(sequence)

    return [(element - smallest) / range_ for element in sequence]