from typing import List

def minSubArraySum(elements_array: List[int]) -> int:
    acc_sum: int = 0
    max_accumulator: int = 0
    idx: int = 0

    while idx < len(elements_array):
        current_val: int = elements_array[idx]
        acc_sum += -current_val  # accumulate negative values to find max subarray sum of negated elements

        if acc_sum < 0:
            acc_sum = 0

        if max_accumulator < acc_sum:
            max_accumulator = acc_sum

        idx += 1

    if max_accumulator == 0:
        negated_elements: List[int] = []
        i: int = 0

        while i < len(elements_array):
            negated_elements.append(-elements_array[i])
            i += 1

        max_accumulator = negated_elements[0]
        j: int = 1
        while j < len(negated_elements):
            if max_accumulator < negated_elements[j]:
                max_accumulator = negated_elements[j]
            j += 1

    result_value: int = -max_accumulator
    return result_value