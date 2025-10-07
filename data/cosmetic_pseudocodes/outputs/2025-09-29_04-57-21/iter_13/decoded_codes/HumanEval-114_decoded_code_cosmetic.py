from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    peak_accumulator: int = 0
    current_aggregate: int = 0

    def ITERATE(index: int) -> None:
        nonlocal current_aggregate, peak_accumulator
        if index >= len(list_of_integers):
            return
        current_aggregate += -list_of_integers[index]
        if current_aggregate < 0:
            current_aggregate = 0
        if current_aggregate > peak_accumulator:
            peak_accumulator = current_aggregate
        ITERATE(index + 1)

    ITERATE(0)

    if peak_accumulator == 0:
        peak_accumulator = max(-x for x in list_of_integers)

    return -peak_accumulator