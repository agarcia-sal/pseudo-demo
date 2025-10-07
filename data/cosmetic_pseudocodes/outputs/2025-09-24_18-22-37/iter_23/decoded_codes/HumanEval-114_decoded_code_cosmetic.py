from typing import Sequence


def minSubArraySum(input_sequence: Sequence[int]) -> int:
    acc_sum: int = 0
    peak_sum: int = 0
    idx: int = 0

    while idx < len(input_sequence):
        val: int = input_sequence[idx]
        neg_val: int = -val
        acc_sum_candidate: int = acc_sum + neg_val
        if acc_sum_candidate < 0:
            acc_sum = 0
        else:
            acc_sum = acc_sum_candidate

        if acc_sum > peak_sum:
            peak_sum = acc_sum
        idx += 1

    if peak_sum == 0:
        neg_values = [-x for x in input_sequence]  # list of negated values
        max_neg_value: int = neg_values[0]
        j: int = 1
        while j < len(neg_values):
            if max_neg_value < neg_values[j]:
                max_neg_value = neg_values[j]
            j += 1
        peak_sum = max_neg_value

    result: int = -peak_sum
    return result