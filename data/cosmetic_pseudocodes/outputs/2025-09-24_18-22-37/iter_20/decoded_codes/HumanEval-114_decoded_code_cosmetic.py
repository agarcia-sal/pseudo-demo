from typing import Sequence

def minSubArraySum(input_sequence: Sequence[int]) -> int:
    accumulator: int = 0
    peak: int = 0
    position: int = 0

    while position < len(input_sequence):
        current_element: int = input_sequence[position]
        invert: int = -current_element
        accumulator += invert
        if accumulator < 0:
            accumulator = 0
        if peak < accumulator:
            peak = accumulator
        position += 1

    if peak == 0:
        inverted_values = [-x for x in input_sequence]
        maximum_inverted = inverted_values[0]
        idx = 1
        length = len(inverted_values)
        while idx < length:
            if maximum_inverted < inverted_values[idx]:
                maximum_inverted = inverted_values[idx]
            idx += 1
        peak = maximum_inverted

    result = -peak
    return result