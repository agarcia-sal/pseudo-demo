from typing import Sequence

def minSubArraySum(sequence: Sequence[int]) -> int:
    idx: int = 0
    acc: int = 0
    peak: int = 0

    while True:
        if idx >= len(sequence):
            break
        acc += -sequence[idx]
        if acc < 0:
            acc = 0
        peak = acc if acc >= peak else peak
        idx += 1

    if peak == 0:
        i: int = 0
        maxNeg: int = -sequence[0]
        while True:
            if i >= len(sequence):
                break
            maxNeg = max(-sequence[i], maxNeg)
            i += 1
        peak = maxNeg

    result: int = -peak
    return result