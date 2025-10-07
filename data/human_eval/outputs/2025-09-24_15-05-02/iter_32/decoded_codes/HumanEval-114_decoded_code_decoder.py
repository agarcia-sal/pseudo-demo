from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    maximum_subarray_sum: int = 0
    current_sum: int = 0
    for integer in list_of_integers:
        current_sum += -integer  # accumulate negated integers
        if current_sum < 0:
            current_sum = 0
        maximum_subarray_sum = max(current_sum, maximum_subarray_sum)
    if maximum_subarray_sum == 0:
        maximum_subarray_sum = max(-integer for integer in list_of_integers)
    minimum_subarray_sum = -maximum_subarray_sum
    return minimum_subarray_sum