from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    acc_sum: int = 0
    max_neg_sum: int = 0

    for element in list_of_integers:
        acc_sum += -element
        if acc_sum < 0:
            acc_sum = 0
        if acc_sum > max_neg_sum:
            max_neg_sum = acc_sum

    if max_neg_sum == 0:
        inverted_elements = [-val for val in list_of_integers]
        max_neg_sum = inverted_elements[0]
        for inverted_val in inverted_elements:
            if inverted_val > max_neg_sum:
                max_neg_sum = inverted_val

    min_sub_sum = -max_neg_sum
    return min_sub_sum