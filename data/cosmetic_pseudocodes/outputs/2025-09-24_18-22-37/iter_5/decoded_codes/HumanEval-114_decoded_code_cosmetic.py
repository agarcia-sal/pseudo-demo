from typing import List

def minSubArraySum(array_of_ints: List[int]) -> int:
    max_so_far: int = 0
    curr_total: int = 0
    index: int = 0
    length: int = len(array_of_ints)

    while index < length:
        current_val: int = array_of_ints[index]
        neg_val: int = -current_val
        curr_total += neg_val
        if curr_total < 0:
            curr_total = 0
        if curr_total > max_so_far:
            max_so_far = curr_total
        index += 1

    if max_so_far == 0:
        neg_values: List[int] = [-x for x in array_of_ints]
        max_neg: int = neg_values[0]
        for j in range(1, len(neg_values)):
            if neg_values[j] > max_neg:
                max_neg = neg_values[j]
        max_so_far = max_neg

    min_sum: int = -max_so_far
    return min_sum