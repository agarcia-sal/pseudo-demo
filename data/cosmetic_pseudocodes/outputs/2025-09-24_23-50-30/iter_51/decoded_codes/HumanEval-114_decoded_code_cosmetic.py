from typing import Sequence

def minSubArraySum(array_of_values: Sequence[int]) -> int:
    acc_sum: int = 0
    peak_sum: int = 0
    for element in array_of_values:
        acc_sum += -element
        if acc_sum < 0:
            acc_sum = 0
        if acc_sum > peak_sum:
            peak_sum = acc_sum
    if peak_sum == 0:
        peak_sum = max(-val for val in array_of_values)
    lowest_sum: int = -peak_sum
    return lowest_sum