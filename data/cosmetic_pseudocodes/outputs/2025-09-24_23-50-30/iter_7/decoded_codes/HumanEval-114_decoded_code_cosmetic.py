from typing import Sequence

def minSubArraySum(input_sequence: Sequence[int]) -> int:
    acc_sum: int = 0
    record_max: int = 0
    idx: int = 0

    while idx < len(input_sequence):
        acc_sum -= input_sequence[idx]
        if acc_sum < 0:
            acc_sum = 0
        if acc_sum > record_max:
            record_max = acc_sum
        idx += 1

    if record_max == 0:
        negatives = [-value for value in input_sequence]
        max_neg = negatives[0]
        pos = 1
        while pos < len(negatives):
            if max_neg < negatives[pos]:
                max_neg = negatives[pos]
            pos += 1
        record_max = max_neg

    return -record_max