from typing import Sequence

def minSubArraySum(input_sequence: Sequence[int]) -> int:
    acc_sum: int = 0
    peak_sum: int = 0
    for val in input_sequence:
        acc_sum += -val
        if acc_sum < 0:
            acc_sum = 0
        peak_sum = acc_sum if acc_sum > peak_sum else peak_sum
    if peak_sum == 0:
        peak_sum = max((-x for x in input_sequence))
    return -peak_sum