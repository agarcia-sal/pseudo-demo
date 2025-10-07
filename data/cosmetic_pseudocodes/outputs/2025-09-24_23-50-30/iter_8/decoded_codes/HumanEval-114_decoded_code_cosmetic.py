from typing import Sequence

def minSubArraySum(sequence: Sequence[int]) -> int:
    acc = 0
    peak = 0
    idx = 0
    sz = len(sequence)
    while idx < sz:
        acc -= sequence[idx]
        if acc < 0:
            acc = 0
        if acc > peak:
            peak = acc
        idx += 1
    if peak == 0:
        peak = sequence[0]
        j = 1
        while j < sz:
            if -sequence[j] > peak:
                peak = -sequence[j]
            j += 1
    return -peak