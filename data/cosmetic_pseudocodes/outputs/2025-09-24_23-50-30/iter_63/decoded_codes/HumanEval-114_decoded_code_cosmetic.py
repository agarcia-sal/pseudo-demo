from typing import Iterable

def minSubArraySum(input_sequence: Iterable[int]) -> int:
    accumulator: int = 0
    peak: int = 0
    for element in input_sequence:
        accumulator += -element
        if accumulator < 0:
            accumulator = 0
        if peak < accumulator:
            peak = accumulator
    if peak == 0:
        peak_candidates = [-item for item in input_sequence]
        peak = peak_candidates[0]
        for candidate in peak_candidates:
            if candidate > peak:
                peak = candidate
    return -peak