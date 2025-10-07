from typing import Sequence

def minSubArraySum(sequence: Sequence[int]) -> int:
    peak: int = 0
    accumulator: int = 0
    for index in range(len(sequence)):
        accumulator += 0 - sequence[index]
        if accumulator < 0:
            accumulator = 0
        if peak < accumulator:
            peak = accumulator
    if peak == 0:
        neg_sequence = (0 - x for x in sequence)
        neg_items = list(neg_sequence)
        peak = neg_items[0]
        for item in neg_items:
            if item > peak:
                peak = item
    return 0 - peak