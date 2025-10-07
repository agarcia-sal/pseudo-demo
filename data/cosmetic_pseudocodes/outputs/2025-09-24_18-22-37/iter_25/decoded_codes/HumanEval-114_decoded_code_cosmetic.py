from typing import Sequence


def minSubArraySum(sequence_of_values: Sequence[int]) -> int:
    peak_total: int = 0
    temp_accumulator: int = 0

    index: int = 0
    length: int = len(sequence_of_values)
    while index < length:
        element: int = sequence_of_values[index]
        temp_accumulator += -element

        if temp_accumulator < 0:
            temp_accumulator = 0

        if peak_total < temp_accumulator:
            peak_total = temp_accumulator

        index += 1

    if peak_total == 0:
        temp_values: list[int] = [-val for val in sequence_of_values]

        max_negative: int = temp_values[0]
        idx2: int = 1
        length_temp = len(temp_values)
        while idx2 < length_temp:
            if temp_values[idx2] > max_negative:
                max_negative = temp_values[idx2]
            idx2 += 1

        peak_total = max_negative

    lowest_sum: int = -peak_total
    return lowest_sum