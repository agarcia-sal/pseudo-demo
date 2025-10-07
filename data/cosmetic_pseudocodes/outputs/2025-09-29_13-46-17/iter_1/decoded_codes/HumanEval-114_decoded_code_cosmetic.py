from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_accumulator: int = 0
    current_accumulator: int = 0
    for element in list_of_integers:
        current_accumulator += -element
        if current_accumulator < 0:
            current_accumulator = 0
        if current_accumulator > max_accumulator:
            max_accumulator = current_accumulator
    if max_accumulator == 0:
        max_accumulator = max(-val for val in list_of_integers)
    min_sum: int = -max_accumulator
    return min_sum