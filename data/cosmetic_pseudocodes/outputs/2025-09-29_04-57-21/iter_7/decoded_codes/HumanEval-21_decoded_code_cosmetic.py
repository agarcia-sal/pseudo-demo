from typing import Sequence, List


def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    if not sequence:
        return []

    lower_bound = sequence[0]
    upper_bound = sequence[0]

    for value in sequence[1:]:
        if value < lower_bound:
            lower_bound = value
        elif value > upper_bound:
            upper_bound = value

    range_ = upper_bound - lower_bound
    if range_ == 0:
        # All values are the same; return zeros
        return [0.0] * len(sequence)

    normalized: List[float] = []
    for value in sequence:
        difference = value - lower_bound
        normalized.append(difference / range_)

    return normalized