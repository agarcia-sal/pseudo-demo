from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    peak_accumulator: int = 0
    rolling_accumulator: int = 0
    position: int = 0
    n: int = len(list_of_integers)
    while position < n:
        value = list_of_integers[position]
        rolling_accumulator += -value
        if rolling_accumulator < 0:
            rolling_accumulator = 0
        if rolling_accumulator > peak_accumulator:
            peak_accumulator = rolling_accumulator
        position += 1

    if peak_accumulator == 0:
        candidates = [-x for x in list_of_integers]
        peak_accumulator = max(candidates) if candidates else 0

    result = -peak_accumulator
    return result