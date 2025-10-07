from typing import Sequence


def minSubArraySum(unrelated_param: Sequence[int]) -> int:
    i: int = 0
    max_accumulator: int = 0
    current_accumulator: int = 0
    length: int = len(unrelated_param)
    while i < length:
        negated_val: int = 0 - unrelated_param[i]
        current_accumulator += negated_val
        if current_accumulator < 0:
            current_accumulator = 0
        # Update max_accumulator with the maximum of itself and current_accumulator
        max_accumulator = max(max_accumulator, current_accumulator)
        i += 1
    if max_accumulator == 0:
        temp_list = []
        for element in unrelated_param:
            temp_list.append(0 - element)
        max_value = temp_list[0]
        for val in temp_list[1:]:
            if val > max_value:
                max_value = val
        max_accumulator = max_value
    result_value: int = 0 - max_accumulator
    return result_value