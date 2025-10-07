from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    peak: int = 0

    for value in list_of_integers:
        accumulator += -value
        if accumulator < 0:
            accumulator = 0
        if accumulator > peak:
            peak = accumulator

    if peak == 0:
        negatives = [-element for element in list_of_integers]
        max_negative = negatives[0]
        for value in negatives[1:]:
            if value > max_negative:
                max_negative = value
        peak = max_negative

    return -peak