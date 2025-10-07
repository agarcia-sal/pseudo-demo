from typing import List

def minSubArraySum(array_of_numbers: List[int]) -> int:
    accumulator: int = 0
    peak: int = 0

    for element in array_of_numbers:
        negated = -element
        accumulator += negated

        if accumulator < 0:
            accumulator = 0

        if accumulator > peak:
            peak = accumulator

    if peak == 0:
        candidates = [-item for item in array_of_numbers]
        peak = candidates[0]
        for index in range(1, len(candidates)):
            if candidates[index] > peak:
                peak = candidates[index]

    result = -peak
    return result