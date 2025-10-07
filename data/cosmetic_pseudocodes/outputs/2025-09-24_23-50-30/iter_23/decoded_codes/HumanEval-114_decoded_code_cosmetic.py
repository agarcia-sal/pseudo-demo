from typing import Sequence

def minSubArraySum(sequence: Sequence[int]) -> int:
    acc: int = 0
    record_max: int = 0

    for element in sequence:
        acc += -element
        if acc < 0:
            acc = 0
        if acc > record_max:
            record_max = acc

    if record_max == 0:
        record_max = max(-x for x in sequence)

    result: int = -record_max
    return result