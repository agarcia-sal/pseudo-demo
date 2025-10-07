from typing import List
import math

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_sum: int = 0
    curr_sum: int = 0
    for number in list_of_integers:
        curr_sum += -number
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
    if max_sum == 0:
        max_sum = -math.inf
        for element in list_of_integers:
            if -element > max_sum:
                max_sum = -element
    minimum_sum: int = -max_sum  # type: ignore
    return minimum_sum