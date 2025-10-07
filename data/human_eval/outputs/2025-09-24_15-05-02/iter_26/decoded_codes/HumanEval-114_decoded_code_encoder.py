from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_sum: int = 0
    current_sum: int = 0
    for number in list_of_integers:
        current_sum += -number
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    if max_sum == 0:
        max_sum = max(-element for element in list_of_integers)
    min_sum: int = -max_sum
    return min_sum