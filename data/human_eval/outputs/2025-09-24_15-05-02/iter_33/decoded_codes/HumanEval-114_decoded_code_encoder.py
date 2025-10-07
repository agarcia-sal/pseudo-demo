from typing import List

def minSubArraySum(list_of_numbers: List[int]) -> int:
    maximum_sum: int = 0
    current_sum: int = 0
    for number in list_of_numbers:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        if current_sum > maximum_sum:
            maximum_sum = current_sum
    if maximum_sum == 0:
        maximum_sum = max(-x for x in list_of_numbers)
    minimum_sum: int = -maximum_sum
    return minimum_sum