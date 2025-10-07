from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    highest_sum: int = 0
    running_sum: int = 0
    iterator: int = 0

    while iterator < len(list_of_integers):
        current_value = list_of_integers[iterator]
        negated_current = -current_value
        running_sum += negated_current
        if running_sum < 0:
            running_sum = 0
        if running_sum > highest_sum:
            highest_sum = running_sum
        iterator += 1

    if highest_sum == 0:
        candidates = [-x for x in list_of_integers]
        max_candidate = candidates[0]
        j = 1
        while j < len(candidates):
            if candidates[j] > max_candidate:
                max_candidate = candidates[j]
            j += 1
        highest_sum = max_candidate

    min_sum_result = -highest_sum
    return min_sum_result