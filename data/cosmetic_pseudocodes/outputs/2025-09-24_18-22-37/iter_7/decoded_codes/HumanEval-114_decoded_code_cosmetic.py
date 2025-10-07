from typing import Sequence

def minSubArraySum(input_sequence: Sequence[int]) -> int:
    accumulator: int = 0
    highest_accumulator: int = 0
    index: int = 0
    length: int = len(input_sequence)
    while index < length:
        current_value: int = input_sequence[index]
        negated_value: int = 0 - current_value
        accumulator += negated_value
        if accumulator < 0:
            accumulator = 0
        if accumulator > highest_accumulator:
            highest_accumulator = accumulator
        index += 1
    if highest_accumulator == 0:
        max_negated_value: int = float('-inf')
        pointer: int = 0
        while pointer < length:
            element: int = input_sequence[pointer]
            negated_element: int = 0 - element
            if negated_element > max_negated_value:
                max_negated_value = negated_element
            pointer += 1
        highest_accumulator = max_negated_value
    minimal_sum: int = 0 - highest_accumulator
    return minimal_sum