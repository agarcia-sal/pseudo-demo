from typing import List

def minSubArraySum(arr: List[int]) -> int:
    acc: int = 0
    peak: int = 0
    idx: int = 0
    length: int = len(arr)
    while idx < length:
        val: int = arr[idx]
        neg_val: int = -val
        temp_sum: int = acc + neg_val
        acc = temp_sum
        if acc < 0:
            acc = 0
        if acc > peak:
            peak = acc
        idx += 1
    if peak == 0:
        neg_values: List[int] = [-x for x in arr]
        max_neg: int = neg_values[0]
        k: int = 1
        n_len: int = len(neg_values)
        while k < n_len:
            if neg_values[k] > max_neg:
                max_neg = neg_values[k]
            k += 1
        peak = max_neg
    result: int = -peak
    return result