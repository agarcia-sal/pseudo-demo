from typing import List

def minSubArraySum(array_elements: List[int]) -> int:
    result_accumulator: int = 0
    running_total: int = 0
    current_position: int = 0

    while current_position < len(array_elements):
        element: int = array_elements[current_position]
        running_total += -element
        if running_total < 0:
            running_total = 0
        if running_total > result_accumulator:
            result_accumulator = running_total
        current_position += 1

    if result_accumulator == 0:
        candidate_values: List[int] = [-e for e in array_elements]
        max_candidate: int = candidate_values[0]
        iterator: int = 1
        while iterator < len(candidate_values):
            if max_candidate < candidate_values[iterator]:
                max_candidate = candidate_values[iterator]
            iterator += 1
        result_accumulator = max_candidate

    lowest_subarray_sum: int = -result_accumulator
    return lowest_subarray_sum