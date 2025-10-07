from typing import List

def minSubArraySum(input_list: List[int]) -> int:
    curr_accumulator: int = 0
    best_accumulator: int = 0
    for idx in range(len(input_list)):
        curr_accumulator += 0 - input_list[idx]
        if curr_accumulator < 0:
            curr_accumulator = 0
        if curr_accumulator > best_accumulator:
            best_accumulator = curr_accumulator
    if best_accumulator == 0:
        negated_values = [0 - elem for elem in input_list]
        best_accumulator = negated_values[0]
        for i in range(1, len(negated_values)):
            if negated_values[i] > best_accumulator:
                best_accumulator = negated_values[i]
    return 0 - best_accumulator