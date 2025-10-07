from typing import List

def minSubArraySum(list_of_numbers: List[int]) -> int:
    maximum_sum = 0
    current_sum = 0
    for number in list_of_numbers:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        maximum_sum = max(current_sum, maximum_sum)
    if maximum_sum == 0:
        maximum_sum = max(-value for value in list_of_numbers)
    minimum_sum = -maximum_sum
    return minimum_sum