from typing import List


def minSubArraySum(array_of_ints: List[int]) -> int:
    max_accumulator: int = 0
    current_accumulator: int = 0
    idx: int = 0
    length: int = len(array_of_ints)
    while True:
        if idx >= length:
            break
        elem: int = array_of_ints[idx]
        negated_elem: int = -elem
        current_accumulator += negated_elem
        if current_accumulator < 0:
            current_accumulator = 0
        if max_accumulator < current_accumulator:
            max_accumulator = current_accumulator
        idx += 1
    if max_accumulator == 0:
        negated_values: List[int] = []
        j: int = 0
        while j < length:
            negated_values.append(-array_of_ints[j])
            j += 1
        max_val: int = negated_values[0]
        k: int = 1
        while k < len(negated_values):
            if negated_values[k] > max_val:
                max_val = negated_values[k]
            k += 1
        max_accumulator = max_val
    answer: int = -max_accumulator
    return answer