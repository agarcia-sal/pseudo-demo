from typing import List

def minSubArraySum(list_of_numbers: List[int]) -> int:
    maximum_sum = 0
    current_sum = 0
    for number in list_of_numbers:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        if current_sum > maximum_sum:
            maximum_sum = current_sum
    if maximum_sum == 0:
        maximum_sum = max(-num for num in list_of_numbers) if list_of_numbers else 0
    minimum_sum = -maximum_sum
    return minimum_sum