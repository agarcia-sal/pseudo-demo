from typing import Sequence, List


def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    low_bound: float = float('inf')
    high_bound: float = float('-inf')

    for value in sequence:
        if value < low_bound:
            low_bound = value
        if value > high_bound:
            high_bound = value

    span: float = high_bound - low_bound

    def normalize_value(value: float) -> float:
        if span == 0:
            return 0.0
        return (value - low_bound) / span

    return [normalize_value(value) for value in sequence]