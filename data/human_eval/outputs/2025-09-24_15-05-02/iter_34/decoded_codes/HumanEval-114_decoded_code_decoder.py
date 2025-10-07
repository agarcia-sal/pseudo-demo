from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    maximum_sum: int = 0
    temporary_sum: int = 0
    for number in list_of_integers:
        temporary_sum += -number
        if temporary_sum < 0:
            temporary_sum = 0
        if temporary_sum > maximum_sum:
            maximum_sum = temporary_sum
    if maximum_sum == 0:
        maximum_sum = max(-x for x in list_of_integers)
    minimum_sum: int = -maximum_sum
    return minimum_sum