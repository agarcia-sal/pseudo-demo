from typing import Iterable

def minSubArraySum(input_sequence: Iterable[int]) -> int:
    acc: int = 0
    peak: int = 0
    for element in input_sequence:
        acc += -element
        if acc < 0:
            acc = 0
        if acc > peak:
            peak = acc
    if peak == 0:
        peak = max(-x for x in input_sequence)
    return -peak