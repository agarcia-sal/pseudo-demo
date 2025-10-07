from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    best_neg_sum: int = 0
    curr_neg_sum: int = 0
    iterator: int = 0
    length: int = len(list_of_integers)
    while iterator < length:
        element: int = list_of_integers[iterator]
        curr_neg_sum += -element
        if curr_neg_sum < 0:
            curr_neg_sum = 0
        if curr_neg_sum > best_neg_sum:
            best_neg_sum = curr_neg_sum
        iterator += 1
    if best_neg_sum == 0:
        best_neg_sum = max(-x for x in list_of_integers)
    minimal_sum: int = -best_neg_sum
    return minimal_sum