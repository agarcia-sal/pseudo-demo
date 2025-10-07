from typing import Sequence

def minSubArraySum(integer_sequence: Sequence[int]) -> int:
    current_accumulator: int = 0
    highest_accumulator: int = 0
    iterator = iter(integer_sequence)

    for current_element in iterator:
        current_accumulator += -current_element
        if current_accumulator < 0:
            current_accumulator = 0
        if highest_accumulator < current_accumulator:
            highest_accumulator = current_accumulator

    if highest_accumulator == 0:
        candidates = [-x for x in integer_sequence]
        highest_accumulator = max(candidates) if candidates else 0

    result_minimum: int = -highest_accumulator
    return result_minimum