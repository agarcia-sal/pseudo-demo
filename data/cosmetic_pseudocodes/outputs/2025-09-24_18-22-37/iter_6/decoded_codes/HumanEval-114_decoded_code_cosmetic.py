from typing import List


def minSubArraySum(array_of_numbers: List[int]) -> int:
    idx: int = 0
    acc_value: int = 0
    peak_value: int = 0
    length: int = len(array_of_numbers)
    while idx < length:
        current_val: int = -array_of_numbers[idx]
        acc_value += current_val
        if acc_value < 0:
            acc_value = 0
        if acc_value > peak_value:
            peak_value = acc_value
        idx += 1

    if peak_value == 0:
        neg_list: List[int] = []
        pos_idx: int = 0
        while pos_idx < length:
            neg_list.append(-array_of_numbers[pos_idx])
            pos_idx += 1

        peak_val_candidate: int = neg_list[0]
        candidate_idx: int = 1
        while candidate_idx < len(neg_list):
            if neg_list[candidate_idx] > peak_val_candidate:
                peak_val_candidate = neg_list[candidate_idx]
            candidate_idx += 1
        peak_value = peak_val_candidate

    result_min_sum: int = -peak_value
    return result_min_sum