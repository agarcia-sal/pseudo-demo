from typing import Sequence


def minSubArraySum(sequence_of_values: Sequence[int]) -> int:
    index_var: int = 0
    accum_value: int = 0
    best_value: int = 0

    length: int = len(sequence_of_values)
    while index_var < length:
        current_val: int = sequence_of_values[index_var]
        accum_value += (0 - current_val)
        if accum_value >= 0:
            if accum_value > best_value:
                best_value = accum_value
        else:
            accum_value = 0
        index_var += 1

    if best_value == 0:
        temp_max: int = -sequence_of_values[0]
        pos: int = 1
        while pos < length:
            neg_val: int = 0 - sequence_of_values[pos]
            if neg_val > temp_max:
                temp_max = neg_val
            pos += 1
        best_value = temp_max

    result: int = 0 - best_value
    return result