from typing import Iterable

def minSubArraySum(sequence_of_values: Iterable[int]) -> int:
    accumulator: int = 0
    peak: int = 0
    for value in sequence_of_values:
        accumulator += -value
        if accumulator < 0:
            accumulator = 0
        if accumulator > peak:
            peak = accumulator
    if peak == 0:
        peak = max(-e for e in sequence_of_values)
    return -peak