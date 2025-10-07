from typing import Sequence

def minSubArraySum(sequence: Sequence[int]) -> int:
    acc: int = 0
    peak: int = 0

    for element in sequence:
        acc += -element
        if acc < 0:
            acc = 0
        if acc > peak:
            peak = acc

    if peak == 0:
        candidates = [-val for val in sequence]
        peak = candidates[0]
        for v in candidates[1:]:
            if v > peak:
                peak = v

    return -peak