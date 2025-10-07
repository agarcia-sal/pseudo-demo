from typing import List


def minSubArraySum(array_of_values: List[int]) -> int:
    acc_sum: int = 0
    best_sum: int = 0
    for current_val in array_of_values:
        delta = 0 - current_val
        acc_sum += delta

        if acc_sum < 0:
            acc_sum = 0

        if acc_sum > best_sum:
            best_sum = acc_sum

    if best_sum == 0:
        neg_candidates = [-val for val in array_of_values]
        best_sum = neg_candidates[0]
        for val in neg_candidates[1:]:
            if val > best_sum:
                best_sum = val

    result_val = 0 - best_sum
    return result_val