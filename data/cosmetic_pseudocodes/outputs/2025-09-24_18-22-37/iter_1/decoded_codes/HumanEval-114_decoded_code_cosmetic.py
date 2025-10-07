from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_sum_found: int = 0
    current_sum: int = 0
    for element in list_of_integers:
        current_sum += -element
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum_found:
            max_sum_found = current_sum
    if max_sum_found == 0:
        max_sum_found = max(-element for element in list_of_integers)
    return -max_sum_found