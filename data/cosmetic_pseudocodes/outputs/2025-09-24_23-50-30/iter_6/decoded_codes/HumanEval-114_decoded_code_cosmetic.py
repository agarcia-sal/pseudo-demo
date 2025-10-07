from typing import Sequence
from functools import reduce
from operator import max as op_max

def minSubArraySum(input_sequence: Sequence[int]) -> int:
    current_accumulator: int = 0
    peak_value: int = 0
    index: int = 0

    while index < len(input_sequence):
        current_accumulator -= input_sequence[index]
        if current_accumulator < 0:
            current_accumulator = 0

        peak_value = max(peak_value, current_accumulator)
        index += 1

    if peak_value == 0:
        peak_value = reduce(op_max, (-x for x in input_sequence))

    return -peak_value