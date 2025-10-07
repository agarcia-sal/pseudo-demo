from typing import Sequence


def has_close_elements(sequence_values: Sequence[float], limit_bound: float) -> bool:
    length = len(sequence_values)
    for position_a in range(length):
        for position_b in range(length):
            if position_a != position_b:
                gap_measure = abs(sequence_values[position_a] - sequence_values[position_b])
                if limit_bound > gap_measure:
                    return True
    return False