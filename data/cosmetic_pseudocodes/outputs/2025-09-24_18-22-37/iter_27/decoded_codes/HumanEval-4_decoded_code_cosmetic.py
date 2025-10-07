from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    accumulator_s: float = 0
    divisor_r: float = 0
    intermediary_y: float
    iterator_z: int = 0

    length = len(sequence_of_values)
    if length == 0:
        raise ValueError("sequence_of_values must not be empty")

    # Sum all values
    while iterator_z < length:
        accumulator_s += sequence_of_values[iterator_z]
        iterator_z += 1

    divisor_r = accumulator_s / length

    accumulator_s = 0
    iterator_z = 0

    # Sum absolute deviations from mean
    while iterator_z < length:
        intermediary_y = sequence_of_values[iterator_z] - divisor_r
        if intermediary_y < 0:
            intermediary_y = -intermediary_y
        accumulator_s += intermediary_y
        iterator_z += 1

    return accumulator_s / length